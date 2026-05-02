import requests

TOKEN = "AAGcUVrvipDUuOkzg4OMzBm7ssrnbls5VWM"
CHAT_ID = "7772436751"

def enviar(msg):
    url = f"https://api.telegram.org/bot{AAGcUVrvipDUuOkzg4OMzBm7ssrnbls5VWM}/sendMessage"
    requests.post(url, data={"7772436751": 7772436751, "text": msg})


# 🔴 señal de no entrar
enviar("🔴 NO JUGAR - mercado inestable")

# 🟢 señal de posible entrada (solo mensaje, no predicción real)
enviar("🟢 POSIBLE MOVIMIENTO - operar con cuidado")
