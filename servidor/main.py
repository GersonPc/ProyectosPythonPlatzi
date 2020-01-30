from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, ingeniero en python egresado de Platzi!'
 
if __name__ == "__main__":
    app.run()