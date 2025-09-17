import psutil
import time

def medir_recursos(segundos=40):
    print("Midiendo uso de CPU y memoria durante", segundos, "segundos...")
    uso_cpu = []
    uso_memoria = []
    for _ in range(segundos):
        uso_cpu.append(psutil.cpu_percent(interval=1))
        uso_memoria.append(psutil.virtual_memory().percent)
    print("Promedio de uso de CPU:", sum(uso_cpu)/len(uso_cpu), "%")
    print("Promedio de uso de memoria:", sum(uso_memoria)/len(uso_memoria), "%")

if __name__ == "__main__":
    medir_recursos()