from flask import Flask, request # 서버 구현을 위한 Flask 객체 import
import pandas as pd

app = Flask(__name__)  

@app.route('/')
def get():  
    
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5005)
