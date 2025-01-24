from flask import Flask
# 建立 Flask 應用程式
app = Flask(__name__)

# 定義路由
@app.route('/test')
def hello_world():
    return "Hello, qwe!"

