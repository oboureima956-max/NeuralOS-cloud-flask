 from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "NeuralOS fonctionne !"

if __name__ == "__main__":
    print("Démarrage serveur...")
    app.run(host="0.0.0.0", port=5000)