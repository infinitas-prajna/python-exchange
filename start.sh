# 多线程启动
gunicorn -w 4 -t 2 'main:app'

# 普通启动
Python main.py