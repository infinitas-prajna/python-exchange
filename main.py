# app/main.py
from flask import Blueprint
from app import app

# 创建一个蓝图
main = Blueprint('main', __name__)

# 定义一个简单的路由和视图函数
@main.route('/')
def index():
    return "Hello, World!"

# 将蓝图注册到 Flask 应用实例上
with app.app_context():
    app.register_blueprint(main)