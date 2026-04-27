import requests
from services.llm import analizar_con_ia
from services.web_search import buscar_en_google
from services.rag import RAG

API_URL = "https://gmcomponents.onrender.com/backend/products/"


# ================================
# OBTENER PRODUCTOS
# ================================
def obtener_productos():
    return requests.get(API_URL).json()


# ================================
# SELECCIÓN POR ID
# ================================
def seleccionar_por_id(productos, cpu_id, gpu_id, ram_id, mb_id, case_id):
    cpu = gpu = ram = mb = case = None

    for p in productos:
        try:
            pid = int(p["id"])
            categoria = p["categoria"].lower()

            if cpu_id and pid == cpu_id and "procesador" in categoria:
                cpu = p

            elif gpu_id and pid == gpu_id and "grafica" in categoria:
                gpu = p

            elif ram_id and pid == ram_id and "ram" in categoria:
                ram = p

            elif mb_id and pid == mb_id and "placa" in categoria:
                mb = p

            elif case_id and pid == case_id and "gabinete" in categoria:
                case = p

        except:
            continue

    return cpu, gpu, ram, mb, case


# ================================
# 🔥 IA PRINCIPAL (ROBUSTA)
# ================================
def run_ia(cpu_id, gpu_id, ram_id, mb_id, case_id):

    productos = obtener_productos()

    rag = RAG()
    rag.construir_indice(productos)

    cpu, gpu, ram, mb, case = seleccionar_por_id(
        productos,
        cpu_id, gpu_id, ram_id, mb_id, case_id
    )

    # ================================
    # COMPONENTES DISPONIBLES
    # ================================
    disponibles = []

    def add(label, obj):
        if obj is not None:
            disponibles.append(f"{label}: {obj['descripcion']}")

    add("CPU", cpu)
    add("GPU", gpu)
    add("RAM", ram)
    add("PLACA MADRE", mb)
    add("GABINETE", case)

    # Si no hay nada seleccionado
    if len(disponibles) == 0:
        return "❌ No se seleccionaron componentes"

    # ================================
    # QUERY INTELIGENTE
    # ================================
    cpu_text = cpu["descripcion"] if cpu else None
    gpu_text = gpu["descripcion"] if gpu else None

    if cpu_text and gpu_text:
        query = f"{cpu_text} vs {gpu_text} bottleneck"
    elif cpu_text:
        query = cpu_text
    elif gpu_text:
        query = gpu_text
    else:
        query = ""

    # ================================
    # RAG + WEB (SAFE)
    # ================================
    contexto_rag = rag.buscar(query) if query else "Sin contexto RAG disponible"
    info_web = buscar_en_google(query) if query else "Sin búsqueda web"

    # ================================
    # CONTEXTO FINAL
    # ================================
    contexto_final = f"""
====================
COMPONENTES SELECCIONADOS
====================
{chr(10).join(disponibles)}

====================
RAG
====================
{contexto_rag}

====================
WEB
====================
{info_web}
"""

    # ================================
    # IA FINAL
    # ================================
    resultado = analizar_con_ia(cpu, gpu, ram, mb, case, contexto_final)

    return resultado


# ================================
# DEBUG LOCAL
# ================================
if __name__ == "__main__":

    print("🔄 TEST IA LOCAL")

    resultado = run_ia(
        cpu_id=44,
        gpu_id=8,
        ram_id=None,
        mb_id=None,
        case_id=None
    )

    print("\n📊 RESULTADO:\n")
    print(resultado)