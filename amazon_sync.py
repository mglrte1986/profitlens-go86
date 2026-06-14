#!/usr/bin/env python3
import json, os, sys
from decimal import Decimal, ROUND_HALF_UP
BASE_DIR = os.path.expanduser("~/profitlens-go86")
INPUT_JSON = os.path.join(BASE_DIR, "activos_digitales.json")
OUTPUT_JSON = os.path.join(BASE_DIR, "inventario_rodamaster_listo.json")
def redondear(v): return float(Decimal(v).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
if not os.path.isfile(INPUT_JSON): sys.exit(f"✘ No existe {INPUT_JSON}")
with open(INPUT_JSON) as f: data=json.load(f)
productos=data["amazon_referencia"]; margen=Decimal(str(data["configuracion"]["margen_rodamaster"]))
inv=[]
for i in productos:
    costo=Decimal(str(i["precio"])); venta=redondear(costo*margen)
    inv.append({"asin":i["asin"],"producto":i["titulo"],"costo_amazon":float(costo),"precio_venta_rodamaster":venta,"status":"Listo para revender"})
    print(f"✔ {i['asin']} | {i['titulo'][:35]:<35} | ${float(costo):>7.2f} → ${venta:>7.2f}")
with open(OUTPUT_JSON,"w",encoding="utf-8") as f: json.dump(inv,f,ensure_ascii=False,indent=2)
print(f"\n✔ Total: {len(inv)} productos\n✔ Archivo: {OUTPUT_JSON}")
