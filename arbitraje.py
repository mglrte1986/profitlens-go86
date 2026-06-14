import asyncio
import aiohttp
import time

# Configuración de mercados a monitorear (Ejemplo base con APIs públicas)
EXCHANGES = {
    "Bitso": "https://api.bitso.com/v3/ticker/?book=btc_mxn",
    "Coinbase": "https://api.coinbase.com/v2/prices/BTC-MXN/spot",
    "Binance_USDT": "https://api.binance.com/api/v3/ticker/price?symbol=BTCTUSD" # Ejemplo de par estable
}

async def fetch_price(session, name, url):
    try:
        async with session.get(url, timeout=3) as response:
            data = await response.json()
            price = 0.0
            
            # Extracción según la estructura de cada API
            if name == "Bitso" and data.get("success"):
                price = float(data["payload"]["last"])
            elif name == "Coinbase":
                price = float(data["data"]["amount"])
            elif name == "Binance_USDT":
                # Conversión simulada o directa si manejas USD/MXN
                price = float(data["price"])
                
            return name, price
    except Exception as e:
        return name, None

async def monitor_arbitrage():
    async with aiohttp.ClientSession() as session:
        print("====== PROFILENS: MONITOREO DE ALTO FLUJO INICIADO ======")
        while True:
            tasks = [fetch_price(session, name, url) for name, url in EXCHANGES.items()]
            results = await asyncio.gather(*tasks)
            
            prices = {name: price for name, price in results if price is not None}
            
            if len(prices) >= 2:
                # Encontrar el mercado más barato y el más caro
                cheapest = min(prices, key=prices.get)
                expensive = max(prices, key=prices.get)
                
                spread = prices[expensive] - prices[cheapest]
                percentage = (spread / prices[cheapest]) * 100
                
                print(f"\n[{time.strftime('%H:%M:%S')}] Analizando oportunidades:")
                for name, price in prices.items():
                    print(f"  - {name}: ${price:,.2f}")
                
                if percentage > 0.5: # Umbral de alerta de ganancia (0.5%)
                    print(f"  ⚠️ ¡ALERTA DE ARBITRAJE! 🔥")
                    print(f"  Comprar en {cheapest} y vender en {expensive}")
                    print(f"  Spread: ${spread:,.2f} ({percentage:.2f}%)")
                else:
                    print(f"  Buscando brechas... Spread máximo: {percentage:.2f}%")
            else:
                print("Esperando respuestas de los servidores...")
                
            await asyncio.sleep(5) # Frecuencia del bucle de rastreo (5 segundos)

if __name__ == "__main__":
    asyncio.run(monitor_arbitrage())
