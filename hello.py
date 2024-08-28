from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def sey_bye():
    return "<p>Bye, World!</p>"

# odpala serwer tylko wtedy kiedy kod jest w tym samym pliku
if __name__ == "__main__":
    app.run()