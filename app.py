from flask import Flask
app = Flask(__name__)

@app.route("/health")
def health():
    return "ok"

@app.route("/")
def home():
    return "Hello from CI/CD pipeline!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

