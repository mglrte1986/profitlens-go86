import json
import sys
import subprocess

def lanzar_publicacion(plataforma, id_producto):
    try:
        with open('/home/hpagente8686/profitlens-go86/activos_digitales.json', 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        producto = next((p for p in datos['productos'] if p['id'] == id_producto), None)
        
        if not producto:
            print(f"❌ ID de producto '{id_producto}' no encontrado en el archivo verídico.")
            return

        # Comando hacia tu terminal de ventas con los datos reales
        comando = [
            "python3", 
            "/home/hpagente8686/profitlens-go86/terminal_ventas.py", 
            plataforma, 
            producto['titulo'], 
            producto['precio'], 
            producto['descripcion']
        ]
        
        subprocess.run(comando)
        
    except Exception as e:
        print(f"❌ Error al procesar la base de datos de activos: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 cargar_activo.py [fb|meli|amazon] [ID_PRODUCTO]")
        sys.exit(1)
    lanzar_publicacion(sys.argv[1], sys.argv[2])
