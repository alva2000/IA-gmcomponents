from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from test_ia import run_ia

app = Flask(__name__, static_folder="frontend")

CORS(app, resources={r"/*": {"origins": "*"}})


# ================================
# FRONTEND
# ================================
@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")


# ================================
# IA ENDPOINT
# ================================
@app.route("/run-ia", methods=["POST", "OPTIONS"])
def run():
    print("🔥 ENDPOINT EJECUTADO")

    try:
        data = request.json
        print("📩 DATA RECIBIDA:", data)

        def safe_int(v):
            if v is None or v == "":
                return None
            return int(v)

        cpu_id = safe_int(data.get("cpu"))
        gpu_id = safe_int(data.get("gpu"))
        ram_id = safe_int(data.get("ram"))
        mb_id = safe_int(data.get("mb"))
        case_id = safe_int(data.get("case"))

        resultado = run_ia(cpu_id, gpu_id, ram_id, mb_id, case_id)

        return jsonify({
            "ok": True,
            "resultado": str(resultado)
        })

    except Exception as e:
        print("❌ ERROR:", e)

        return jsonify({
            "ok": False,
            "error": str(e)
        })


if __name__ == "__main__":
    print("🚀 SERVER INICIADO http://127.0.0.1:5000")
    app.run(debug=True, port=5000)