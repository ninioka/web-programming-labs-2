from flask import Blueprint, url_for, redirect, render_template, request
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'


flower_list =  [
    {'name': 'Роза', 'price': 150},
    {'name': 'Тюльпан', 'price': 80},
    {'name': 'Незабудка', 'price': 50},
    {'name': 'Ромашка', 'price': 30}
]


#Меню всех цветов
@lab2.route('/lab2/all_flowers/')
def all_flowers():
    flowers = flower_list
    flowers_num = len(flower_list)
    return render_template('lab2/lab2_flowers.html', flower_list=flowers, flowers_num=flowers_num)


# @lab2.route('/lab2/add_flower/<name>/<int:price>/')
# def add_flower(name, price):
#     flower_list.lab2end({'name': name, 'price': price})
#     flowers_num = len(flower_list)
#     return render_template('lab2/add_flower.html', name=name, price=price, flowers_num=flowers_num)


# @lab2.route('/lab2/add_flower/')
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
@lab2.route('/lab2/add_flower/')
def add_flowers():
    name = request.args.get('name')
    price = request.args.get('price')
    style = url_for("static", filename="main.css")
    if name and price:
        flower_list.append({'name': name, 'price': int(price)})
        flower_id = len(flower_list) - 1
        return render_template('lab2/add_flower.html', flower_id=flower_id, name=name, price=price)
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
@lab2.route('/lab2/flowers/<int:flower_id>')
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
    return render_template('lab2/flowers_id.html', flower=flower, flower_id=flower_id)


#Не задан ID цветка
@lab2.route('/lab2/flowers/')
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
@lab2.route('/lab2/delete_flowers/')
def delete_flowers():
    flower_list.clear()  
    return redirect('/lab2/all_flowers/')


#Удалить цветок по ID
@lab2.route('/lab2/delete_flower/<int:flower_id>')
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


@lab2.route('/lab2/example')
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
    return render_template('lab2/example.html', name=name, lab_num=lab_num, group=group, course_number=course_number, fruits=fruits)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase = phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    num_a = a
    num_b = b
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Деление на ноль"
    power = a ** b
    return render_template('lab2/calc.html', a=num_a, b=num_b, addition=addition, subtraction=subtraction,
                           multiplication=multiplication, division=division, power=power)


@lab2.route('/lab2/calc/')
def red_calc():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
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


@lab2.route('/lab2/books/')
def book():
    return render_template('lab2/books.html', books=books)


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


@lab2.route('/lab2/cats/')
def cat():
    return render_template('lab2/cats.html', cats=cats)