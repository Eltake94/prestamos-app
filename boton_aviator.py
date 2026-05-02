historial = []

def analizar():
    if len(historial) < 5:
        print("Esperando más datos...\n")
        return

    ultimas = historial[-10:]
    bajas = len([x for x in ultimas if x < 2])
    altas = len([x for x in ultimas if x >= 2])

    print("\n📊 Últimas:", ultimas)

    if bajas >= 7:
        print("🔴 NO JUGAR\n")
    elif altas >= 6:
        print("🟢 ENTRAR RÁPIDO (1.3x - 1.5x)\n")
    else:
        print("🟡 CUIDADO\n")


print("CONTROLES:")
print("1 = baja (<2x)")
print("2 = alta (>=2x)")
print("0 = salir\n")

while True:
    tecla = input("👉 Presiona tecla: ")

    if tecla == "1":
        historial.append(1.5)  # valor simbólico bajo
    elif tecla == "2":
        historial.append(2.5)  # valor simbólico alto
    elif tecla == "0":
        break
    else:
        print("Tecla inválida\n")
        continue

    analizar()
