def detectar_cuello(cpu, gpu, ram):
    cpu_score = cpu.get("score", 0)
    gpu_score = gpu.get("score", 0)
    ram_gb = ram.get("capacidad", 0)

    ratio = gpu_score / cpu_score if cpu_score > 0 else 0

    if ratio > 1.5:
        return {
            "estado": "CPU_LIMIT",
            "mensaje": "La GPU es mucho más potente que la CPU"
        }
    elif ratio < 0.7:
        return {
            "estado": "GPU_LIMIT",
            "mensaje": "La CPU es mucho más potente que la GPU"
        }
    elif ram_gb < 16:
        return {
            "estado": "RAM_LIMIT",
            "mensaje": "La memoria RAM es insuficiente"
        }
    else:
        return {
            "estado": "BALANCED",
            "mensaje": "Configuración equilibrada"
        }
    

def detectar_cuello(cpu, gpu, ram):
    return "Análisis delegado a IA"