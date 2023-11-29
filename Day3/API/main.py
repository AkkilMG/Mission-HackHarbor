from flask import Flask
app = Flask(__name__)

# pip install flask

@app.route('/')
def hello_world():
    return 'Hello, World!'

# cd ./Day3/API
# python main.py
if __name__ == '__main__':
    app.run()