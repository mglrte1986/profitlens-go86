import asyncio
from playwright.async_api import async_playwright
import json
import os
FB_USER = "tu_correo_de_facebook@gmail.com"
FB_PASS = "tu_contraseña_real_o_token"

async def publicar_en_facebook():
    if not os.path.exists("productos.json"):
        print("❌ Error: Falta productos.json")
        return
    with open("productos.json", "r") as f:
        try: productos = json.load(f)
        except: return
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.facebook.com/login")
        await page.fill("#email", FB_USER)
        await page.fill("#pass", FB_PASS)
        await page.click('button[name="login"]')
        await page.wait_for_timeout(5000)
        for prod in productos:
            if prod.get("precio_venta", "0.00") == "0.00":
                print(f"⚠️ Saltando {prod.get('nombre')} - Sin precio real.")
                continue
            print(f"📦 Publicando de forma real: {prod['nombre']}")
            await page.goto("https://www.facebook.com/sharer/sharer.php?u=https://www.amazon.com.mx")
            await page.wait_for_timeout(3000)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(publicar_en_facebook())
