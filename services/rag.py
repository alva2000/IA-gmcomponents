from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

class RAG:
    def __init__(self):
        self.textos = []
        self.index = None

    def construir_indice(self, productos):
        self.textos = [
            f"{p['categoria']} {p['nombre']} {p['descripcion']}"
            for p in productos
        ]

        embeddings = model.encode(self.textos)
        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))

    def buscar(self, query, k=3):
        query_embedding = model.encode([query])
        distancias, indices = self.index.search(query_embedding, k)

        resultados = [self.textos[i] for i in indices[0]]
        return "\n".join(resultados)