import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"

def analizar_con_ia(cpu, gpu, ram, mb, case, contexto):
    prompt = f"""
Eres un experto en hardware especializado en análisis de rendimiento.

VERIFICA QUE LOS COMPONENTES REALES EXISTAN EN LA REALIDAD, NO TE BASES SOLO EN LA INFORMACIÓN DE LA BASE DE DATOS (urlAPI), USA LA INFORMACIÓN DE INTERNET PARA VALIDAR SU EXISTENCIA. SI EL COMPONENTE NO EXISTE, INDÍCALO CLARAMENTE, SI EL COMPONENTE EXISTE, NO DEBES MENCIONAR SU EXISTENCIA DE MANERA EXPLICITA.
CPU: {cpu['descripcion']}
GPU: {gpu['descripcion']}
RAM: {ram['descripcion']}
PLACA MADRE: {mb['descripcion']}
GABINETE: {case['descripcion']}
Contexto:
{contexto}

INSTRUCCIONES:
- Analiza TODOS los datos entregados (API, RAG e internet).
- NO menciones internet ni fuentes externas.
- Tienes PROHIBIDO decir "según la información encontrada en la web" o algo similar, sea en ingles o español."
- Considera analizar las velocidades (mhz), clocks, chipset, generación, tipo de memoria (DDR3, DDR4, DDR5, etc.), tipo de memoria grafica (GDDR5, GDDR6, etc.), el tipo de generacion de RAM con el procesador, y compatibilidad con todo el sistema (grafica, procesadoor, ram, y placa madre), cantidad de nucleos y hilos del procesador, y la arquitectura de la grafica (CUDA,TURING, LOVELACE)
- Usa criterio técnico real.
- Responde como experto.
- Sé claro, directo, y profesional, no te vayas por las ramas.
- Tienes que explicar con tanta sencilles para que un niño lo entienda, pero sin perder el rigor técnico.
- Las soluciones que puedes dar tienen que solo basarse en los componentes entregados, no puedes recomendar comprar otro componente que no forme parte de la base de datos (urlAPI).
- Tienes que recomendar una recomendacion SI O SI, a no ser que sea critico para el sistema, en cuyo caso tienes que recomendar una solución basada en acciones del propio usuario.
- Lee y analiza con atención TODOS los detalles/caracteristicas de los componentes, si el componente indica ghz de 3.0 base y 4.5 turbo, tienes que analizar ambos, no solo el turbo.
- Si aparece en la base de datos (urlAPI) no des por hecho que existe en la realidad, basate en la busqueda en linea para ver la veracidad de los datos (ryzen 2 pro no existe, i4 9200f no existe)
- Solo usa informacion VERIDICA y REAL de internet para validar la existencia de los componentes, no asumas nada que no esté confirmado.

===================
REGLAS ESTRICTAS
===================
- NO inventes especificaciones técnicas
- NO supongas datos que no estén presentes
- Si aparece que el componente no existe, dejarlo indicado.
- Basandote en los datos de internet, indicar si el componente es real o no.


Debes mostrar como respuesta SOLAMENTE estos apartados sin olvidar todo lo razonado anteriormente, sin agregar nada más:
Responde:
1. ¿Hay cuello de botella?
2. Explicación técnica corta de por qué sí o no.
3. Indicar si es un cuello de botella crítico o no crítico (si es crítico, el sistema no funcionará bien hasta que se solucione, si no es crítico, el sistema funcionará pero no al máximo potencial)
4. Recomendación corta
5. Puntaje de compatibilidad (0 a 100)
6. Mostrar listado de los componentes seleccionados además de su compatibilidad (indicar en un parentesis a que tipo de componente pertenece, ya sea CPU, GPU, RAM, PLACA MADRE o GABINETE).
7. (EXCLUSIVAMENTE RESPONDER SI HAY UN COMPONENTE QUE NO EXISTE EN LA REALIDAD) Indicar claramente cuál o cuáles componentes no existen, y basarse en la información de internet para validar su existencia, no asumir nada que no esté confirmado.
"""

    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )

    return res.choices[0].message.content