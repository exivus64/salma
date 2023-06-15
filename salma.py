from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Salma is clever girl</h1><br>Hello salma oni-chan! '

if __name__ == '__main__':
    app.run()