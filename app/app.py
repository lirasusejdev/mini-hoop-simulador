from flask import Flask, jsonify
import os

app = Flask(__name__)
instance_name = os.environ.get("INSTANCE_NAME", "desconhecida")

@app.route("/")
def index():
    return f"Você está na instância: {instance_name}"

@app.route("/deal")
def deal():
    return jsonify({"instance": instance_name, "result": "Comando 'deal' executado!"})

@app.route("/ap")
def ap():
    return jsonify({"instance": instance_name, "result": "Comando 'ap' executado!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)