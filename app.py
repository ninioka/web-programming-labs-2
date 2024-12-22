from flask import Flask, url_for, redirect, render_template, request
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users
from flask_login import LoginManager

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
from rgz import rgz


app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'nina_demchenko_orm'
    db_user = 'nina_demchenko_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "nina_demchenko_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
app.register_blueprint(rgz)


@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename="lab1/404.jpg")
    return '''
<!doctype html>
<html>
    <head>
        <style>
            img {
                width: 70%;
                margin-top: 3px;
            }
            body {
                text-align: center;
                color: rgb(124,166,216);
                background-color: rgb(219,201,191);
                font-size: 26pt;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            }
        </style>
    </head>
    <body>
        <p>Ой... Мы не можем найти эту страницу :(<br>Попробуйте позже!</p><br>
        <img src="'''+ path +'''"><br>
    </body>
</html>
''', 404

@app.route("/")
@app.route("/index")
def main():
    style = url_for("static", filename = "lab1/style.css")
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>  
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            <link rel="stylesheet" type="text/css" href="''' + style + '''">
        </header>
        <main>
            <ul>
                <li><a href = "/lab1">Первая лабораторная</a></li>
                <li><a href = "/lab2/">Вторая лабораторная</a></li>
                <li><a href = "/lab3/">Третья лабораторная</a></li>
                <li><a href = "/lab4/">Четвертая лабораторная</a></li>
                <li><a href = "/lab5/">Пятая лабораторная</a></li>
                <li><a href = "/lab6/">Шестая лабораторная</a></li>
                <li><a href = "/lab7/">Седьмая лабораторная</a></li>
                <li><a href = "/lab8/">Восьмая лабораторная</a></li>
                <li><a href = "/lab9/">Девятая лабораторная</a></li>
                <li><a href = "/rgz/">РГЗ</a></li>
            </ul>
        </main>
        <footer>
            &copy; Нина Демченко, ФБИ-22, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.errorhandler(500)
def interceptor(err):
    return '''
<!doctype html>
<head>
    <style>
        body {
            font-family: 'Pacifico', cursive;
            background-color: #c5bdbd;
            margin-top: 250px;
            text-align: center;
            font-size: 25px;
        }
        h1 {
            color: #b3725c;
            margin-bottom: 10px;
        }
        p {
            color: #797575;
        }
    </style>
</head>
<body>
    <h1>Ошибка сервера.</h1>
    <p>На сервере произошла ошибка. Можете не ждать, она исправлена не будет. ИЗВИНИТЕ!</p>
</body>
</html>''', 500

#Лабораторная работа 2

@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list =  [
    {'name': 'Роза', 'price': 150},
    {'name': 'Тюльпан', 'price': 80},
    {'name': 'Незабудка', 'price': 50},
    {'name': 'Ромашка', 'price': 30}
]

#Меню всех цветов
@app.route('/lab2/all_flowers/')
def all_flowers():
    flowers = flower_list
    flowers_num = len(flower_list)
    return render_template('lab2_flowers.html', flower_list=flowers, flowers_num=flowers_num)

# @app.route('/lab2/add_flower/<name>/<int:price>/')
# def add_flower(name, price):
#     flower_list.append({'name': name, 'price': price})
#     flowers_num = len(flower_list)
#     return render_template('add_flower.html', name=name, price=price, flowers_num=flowers_num)

# @app.route('/lab2/add_flower/')
# def err_add_flower():
#     style = url_for("static", filename="main.css")
#     return '''
# <!doctype html>
# <html>
#     <head>
#         <link rel="stylesheet" type="text/css" href="''' + style + '''">
#     </head>
#     <body>
#         <h1>Вы не задали имя цветка!</h1>
#     </body>
# </html>
# ''', 400

#Добавление цветка
@app.route('/lab2/add_flower/')
def add_flowers():
    name = request.args.get('name')
    price = request.args.get('price')
    style = url_for("static", filename="main.css")
    if name and price:
        flower_list.append({'name': name, 'price': int(price)})
        flower_id = len(flower_list) - 1
        return render_template('add_flower.html', flower_id=flower_id, name=name, price=price)
    else:    
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Поле не заполнено!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 400

#Цветок по ID
@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    style = url_for("static", filename="main.css")
    if flower_id >= len(flower_list):
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Такого цветка нет!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 404
    else:
        flower = flower_list[flower_id]
    return render_template('flowers_id.html', flower=flower, flower_id=flower_id)

#Не задан ID цветка
@app.route('/lab2/flowers/')
def err_flowers():
    style = url_for("static", filename="main.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Вы не задали ID цветка!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 400

#Очистить весь список цветов
@app.route('/lab2/delete_flowers/')
def delete_flowers():
    flower_list.clear()  
    return redirect('/lab2/all_flowers/')

#Удалить цветок по ID
@app.route('/lab2/delete_flower/<int:flower_id>')
def delete_flower(flower_id):
    style = url_for("static", filename="main.css")
    if flower_id >= len(flower_list):
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Цветов больше нет!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 404
    else:
        del flower_list[flower_id]
        return redirect('/lab2/all_flowers/')

@app.route('/lab2/example')
def example():
    name = 'Нина Демченко'
    lab_num = '2'
    group = 'ФБИ-22'
    course_number = '3'
    fruits = [
        {'name': 'Яблоки', 'price': 100}, 
        {'name': 'Груши', 'price': 120}, 
        {'name': 'Апельсины', 'price': 80}, 
        {'name': 'Мандарины', 'price': 95}, 
        {'name': 'Манго', 'price': 321}
        ]
    return render_template('example.html', name=name, lab_num=lab_num, group=group, course_number=course_number, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    num_a = a
    num_b = b
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Деление на ноль"
    power = a ** b
    return render_template('calc.html', a=num_a, b=num_b, addition=addition, subtraction=subtraction,
                           multiplication=multiplication, division=division, power=power)

@app.route('/lab2/calc/')
def red_calc():
    return redirect('/lab2/calc/1/1')

@app.route('/lab2/calc/<int:a>')
def redi_calc(a):
    return redirect(f'/lab2/calc/{a}/1')

books = [
    {"author": "Маргарет Митчелл", "title": "Унесенные ветром", "genre": "Роман", "pages": 992},
    {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 680},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 384},
    {"author": "Олдос Хаксли", "title": "О дивный новый мир", "genre": "Антиутопия", "pages": 352},
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Роман-антиутопия", "pages": 320},
    {"author": "Марк Твен", "title": "Приключения Тома Сойера", "genre": "Повесть", "pages": 336},
    {"author": "Дж. Д. Сэлинджер", "title": "Над пропастью во ржи", "genre": "Роман", "pages": 224},
    {"author": "Маргарет Этвуд", "title": "Рассказ служанки", "genre": "Антиутопия", "pages": 310},
    {"author": "Иван тургенев", "title": "Отцы и дети", "genre": "Роман", "pages": 416},
    {"author": "Рэй Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Научная фантастика", "pages": 174}
]

@app.route('/lab2/books/')
def book():
    return render_template('books.html', books=books)

cats = [
    {
        "name": "Шотландская вислоухая",
        "description": "Отличительная особенность скоттиш фолдов — ее уши. Они небольшого размера и свернуты по направлению к ушному проходу. Кончики ушей имеют круглую форму.",
        "image": "cat1.png"
    },
    {
        "name": "Сфинкс",
        "description": "Главная особенность сфинкса — отсутствие шерсти. Однако кошки не совсем безволосы, а покрыты тонкой пушистой шерстью, похожей на кожуру персика. У этой кошки нет ни усов, ни ресниц.",
        "image": "cat2.png"
    },
    {
        "name": "Манчкин",
        "description": "Манчкины — коротконогие кошки с длинным туловищем, напоминающие такс. Они не обладают знаменитой кошачьей грацией, но очаровывают своим необычным внешним видом.",
        "image": "cat3.png"
    },
    {
        "name": "Саванна",
        "description": "Саванна — высокая худая кошка с длинными лапами. У этих кошек широкий нос и глаза с нависающими веками. На коротких хвостах — черные кольца и однотонный черный кончик.",
        "image": "cat4.png"
    },
    {
        "name": "Сиамская",
        "description": "Сиамская кошка — это кошка среднего размера с длинным, стройным и грациозным телом.  Цвет глаз при любых окрасах и вариантах пятнистости всегда остается ярким, насыщенно-голубым.",
        "image": "cat5.png"
    }
]
@app.route('/lab2/cats/')
def cat():
    return render_template('cats.html', cats=cats) 