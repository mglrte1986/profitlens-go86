#!/usr/bin/env python3
import json, os, sys

JSON_PATH = os.path.expanduser("~/profitlens-go86/activos_digitales.json")

def cargar():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def buscar_producto(termino, data):
    termino = termino.lower()
    resultados = []
    for p in data.get("productos", []):
        if termino in p["nombre"].lower() or termino in p["sku"].lower():
            resultados.append(("Rodamaster", p))
    for a in data.get("amazon_referencia", {}).get("items", []):
        if termino in a["categoria"].lower() or termino in a["ejemplo"].lower():
            resultados.append(("Amazon", a))
    return resultados

def responder(query):
    data = cargar()
    res = buscar_producto(query, data)
    if not res:
        return f"No encontré '{query}'. Prueba con: tenis, freidora, proteína, skincare."

    out = []
    for origen, item in res:
        if origen == "Rodamaster":
            out.append(f"🔧 RODAMASTER 86 – {item['nombre']}\nPrecio: ${item['precio']} MXN\nGarantía: {item['garantia']}\nStock: {item['stock']}")
        else:
            # busca equivalente Rodamaster para comparar
            equiv = next((p for p in data["productos"] if query in p["nombre"].lower()), None)
            comp = f"\n→ Nosotros: ${equiv['precio']} MXN (ahorras ${item['precio_amazon'] - equiv['precio']})" if equiv else ""
            out.append(f"📦 AMAZON MX – {item['ejemplo']} ({item['categoria']})\nPrecio ref: ${item['precio_amazon']} MXN{comp}")
    return "\n\n".join(out)

if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("¿Qué buscas? ")
    print(responder(q))
