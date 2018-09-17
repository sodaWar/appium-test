# coding=utf-8
from flask import Flask                                                                                                 #  导入Flask类

app = Flask(__name__)                                                                                                   #  创建Flask实例,Flask实例是可调用的(具有call方法),这个实例可以直接对接WSGI服务器

# 注册路由,注册路由就是建立URL规则和处理函数之间的关联,Flask框架依赖于路由完成HTTP请求的分发,路由中的函数被视为视图函数,其返回值将作为HTTP响应的正文内容
@app.route('/')
# 路由顾名思义就是在迷茫中找出一条路的意思,在Flask框架中,路由表示为用户请求的URL找出其对应的处理函数之意.在Flask应用中,路由就是指用户请求的URL与视图函数之间的映射
def hello_world():
    return 'Hello world!'

@app.route('/flask')                                                                                                    # 所谓路由即URL绑定,Flask使用route()装饰器将一个函数绑定到一个URL上
def flaskPage():
    return 'Flask Page'

#  route()函数不仅能够绑定路由,还能动态变化URL的某些部分,运行程序后在浏览器中输入http://127.0.0.1:8081/user/HongNaiWu,将会返回Hello HongNaiWu
# @app.route('/user/<user>')
# def test(user):
#     return 'Hello %s' % user

@app.route('/<user>', methods=['POST'])
def test(user):
    return 'Hello %s' % user

def test1():
    print("this is a test code too")

def test2():
    print("i thik life is beautiful")

def test3():
    print("but life is bad to me and it bug")

def myTest1():
    print("it is my test1 function")

def myTest2():
    print("it is my test2 function")

def myTest3():
    print("it is my test3 function")

def myTest4():
    print("it is my test4 function")

def myTest5():
    print("it is my test5 function")

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8081')                                                                               #  对接并启动WSGI服务器


