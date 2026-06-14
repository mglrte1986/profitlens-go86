#!/usr/bin/env python3
import json, os, datetime

JSON_PATH = os.path.expanduser("~/profitlens-go86/activos_digitales.json")

# Lista curada 2026 – fuentes: Amazon MX best sellers + Shopify México【1515886471200077344†L35-L48】【1515886471200077344†L75-L82】
BEST_SELLERS_MX = [
    {"categoria": "Ropa casual", "ejemplo": "Playera básica", "precio_amazon": 299},
    {"categoria": "Tenis y calzado urbano", "ejemplo": "Tenis deportivo", "precio_amazon": 899},
    {"categoria": "Skincare y maquillaje", "ejemplo": "Parches para acné", "precio_amazon": 199},
    {"categoria": "Perfumes y fragancias", "ejemplo": "Perfume 100ml", "precio_amazon": 749},
    {"categoria": "Accesorios moda y joyería", "ejemplo": "Pulsera acero", "precio_amazon": 159},
    {"categoria": "Snacks y alimentos instantáneos", "ejemplo": "Proteína suero", "precio_amazon": 649},
    {"categoria": "Celulares, fundas y accesorios", "ejemplo": "Funda Samsung A17", "precio_amazon": 249},
    {"categoria": "Freidoras de aire y cocina", "ejemplo": "Freidora 4L", "precio_amazon": 1899},
    {"categoria": "Limpieza y hogar", "ejemplo": "Jabón multiusos", "precio_amazon": 129},
    {"categoria": "Organización y decoración", "ejemplo": "Vaso aislante", "precio_amazon": 349},
    {"categoria": "Productos mascotas", "ejemplo": "Alimento perro 5kg", "precio_amazon": 589},
    {"categoria": "Artículos para entrenar", "ejemplo": "Mancuernas 5kg", "precio_amazon": 499},
    {"categoria": "Farmacéuticos y salud", "ejemplo": "Vitaminas", "precio_amazon": 279},
    {"categoria": "Electrónica", "ejemplo": "Protector sobretensiones", "precio_amazon": 399},
]

def pull():
    if not os.path.exists(JSON_PATH):
        print("❌ No encuentro activos_digitales.json")
        return
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["amazon_referencia"] = {
        "actualizado": datetime.datetime.now().isoformat(),
        "fuente": "Amazon MX best sellers 2026",
        "items": BEST_SELLERS_MX
    }

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Pull completo: {len(BEST_SELLERS_MX)} categorías inyectadas")
    print("Listo para vender con margen Rodamaster 86")

if __name__ == "__main__":
    pull()
