from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Everyone! This is my 1st website!"

if __name__ == "__main__":
    app.run( port=8000)
