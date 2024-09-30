from flask import Flask, url_for, redirect, render_template, request
app = Flask(__name__)

@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
            <body>
                <h1>web-сервер на flask</h1>
                <a href="/author">author</a>
            </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
            }

@app.route("/lab1/author")
def author():
    name = "Демченко Нина Николаевна"
    group = "ФБИ-22"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">Web</a>
            </body>
        </html>"""

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    path1 = url_for("static", filename = "lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + path1 + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''<br>
        <a href = "/lab1/reset">Очистить счетчик</a>
    </body>
</html>
'''
@app.route("/lab1/reset")
def reset_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        <a href = "/lab1/counter">Возобновить счетчик</a>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201

@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename="404.jpg")
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
    style = url_for("static", filename = "style.css")
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
            </ul>
        </main>
        <footer>
            &copy; Нина Демченко, ФБИ-22, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1")
def lab1():
    style = url_for("static", filename = "style.css")
    return '''
<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
        <style>
            div {
                text-align: justify;
                font-size: 18pt;
                line-height: 1.25;
                text-indent: 50px;
                margin: 15px;
                font-family: Arial, Helvetica, sans-serif;
            }
            h2 {
                text-align: justify;
                font-size: 18pt;
                margin: 15px;
                font-family: Arial, Helvetica, sans-serif;
            }
            li {
                font-size: 16pt;
                margin-left: 15px;  
            }
        </style>  
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            <link rel="stylesheet" type="text/css" href="''' + style + '''">
        </header>
        <main>
            <div>
                Flask — фреймворк для создания веб-приложений на языке 
                программирования Python, использующий набор инструментов 
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так 
                называемых микрофреймворков — минималистичных каркасов 
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.<br>
            </div>
            <ul>
            <li><a href = '/'>Главная страница</a></li>
            </ul>
            <h2>Список роутов:</h2>
            <ul>
                <li><a href="/lab1/web">Web</a><br></li>
                <li><a href="/lab1/author">Author</a><br></li>
                <li><a href="/lab1/oak">Oak</a><br></li>
                <li><a href="/lab1/counter">Counter</a><br></li>
                <li><a href="/lab1/reset">Reset</a><br></li>
                <li><a href="/lab1/info">Info</a><br></li>
                <li><a href="/lab1/created">Created</a><br></li>
                <li><a href="/404">Ошибка 404</a><br></li>
                <li><a href="/lab1/bad_request">Ошибка 400. Bad request</a><br></li>
                <li><a href="/lab1/unauthorized">Ошибка 401. Unauthorized</a><br></li>
                <li><a href="/lab1/payment_required">Ошибка 402. Payment required</a><br></li>
                <li><a href="/lab1/forbidden">Ошибка 403. Forbidden</a><br></li>
                <li><a href="/lab1/method_not_allowed">Ошибка 405. Method not allowed</a><br></li>
                <li><a href="/lab1/i_am_a_teapot">Ошибка 418. I am a teapot</a><br></li>
                <li><a href="/lab1/internal_server_error">Ошибка 500. Internal server error</a><br></li>
                <li><a href="/lab1/text">Text</a><br></li>
                <li><a href="/lab1/source">Tree</a></li>
            </ul>
        </main>
        <footer>
            &copy; Нина Демченко, ФБИ-22, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/bad_request")
def bad_request():
    return "400 Bad Request. Неправильный запрос.", 400

@app.route("/lab1/unauthorized")
def unauthorized():
    return "401 Unauthorized. Для доступа требуется аутентификация.", 401

@app.route("/lab1/payment_required")
def payment_required():
    return "402 Payment Required. Для доступа необходимо совершить платёж.", 402

@app.route("/lab1/forbidden")
def forbidden():
    return "403 Forbidden. В доступе на данную страницу отказано.", 403

@app.route("/lab1/method_not_allowed")
def method_not_allowed():
    return "405 Method Not Allowed. Указанный метод нельзя применить к текущему ресурсу.", 405

@app.route("/lab1/i_am_a_teapot")
def i_am_a_teapot():
    return "I am a teapot. Сервер отказался варить кофе, потому что он чайник.", 418



@app.route('/lab1/internal_server_error')
def internal_server_error():
    error = "Ошибка!" + 15
    return 'Результат: ' + str(error)

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

@app.route("/lab1/text")
def text():
    path = url_for("static", filename="text.jpg")
    return '''
<!doctype html>
<html>
    <head>
        <style>
            h1, h2 {
                text-align: center;
                margin: 5px;
            }
            div {
                text-align: justify;
                font-size: 18pt;
                line-height: 1.25;
                text-indent: 50px;
                margin: 15px;
            }
            body {
                background-color: rgb(122,89,61);
                text-align: center;
            }
            img {
                width: 70%;
                margin: auto;
            }
        </style>
    </head>
    <body>
        <h2>Джордж Мартин</h2>        
        <h1>Игра престолов. Часть I</h1>
        <div>
            Дэйнерис родилась на Драконьем Камне девять лун спустя после бегства, в жуткую летнюю бурю, едва не уничтожившую островную твердыню. 
            Говорили, что шторм был ужасен. Стоявший на якоре флот Таргариенов разбился о скалы. 
            Волны выворотили из парапетов огромные каменные блоки и выкинули их в бурные волны Узкого моря. 
            Мать умерла, рожая ее. Этого брат так и не простил Дэйнерис.
        </div>
        <div>
            Она не помнила и Драконьего Камня. Потом они снова бежали, как раз перед тем, как брат узурпатора поставил паруса на своем заново отстроенном флоте. 
            К тому времени у Таргариенов от Семи Королевств остался лишь Драконий Камень, древнее гнездо рода. Долго это положение не могло сохраниться. 
            Гарнизон уже был готов продать детей узурпатору, но однажды ночью сир Уиллем Дарри с четверкой верных ему людей ворвался в детскую, 
            выкрал их обоих вместе с кормилицей и под покровом темноты отплыл к безопасному Браавосу.
        </div>
        <div>
           Она смутно помнила сира Уиллема, казавшегося ей огромным седым медведем, полуслепого, громкоголосого, выкрикивающего приказы с ложа. 
           Слуги до ужаса боялись его, но с Дэни он всегда был ласков. Он называл ее крохотной принцессой, иногда своей госпожой, и его ладони были мягкими, как старая кожа. 
           Впрочем, он никогда не покидал постели, запах хвори не оставлял его день и ночь – жаркий, влажный, болезненно сладкий. 
           Так было, пока они жили в Браавосе, в большом доме с красной дверью. У Дэни там была собственная комната с лимонным деревом под окном. 
           После того как сир Уиллем умер, слуги украли те небольшие деньги, которые оставались у них, и детей скоро выставили из большого дома. 
           Дэни плакала, когда красная дверь навсегда закрылась за ними. После этого они скитались – из Браавоса в Мир, из Мира в Тирош, а потом в Квохор, 
           Волантис и Лисс, не задерживаясь подолгу на одном месте. Брат твердил, что их преследуют нанятые узурпатором наемные убийцы, 
           хотя Дэни так и не видела ни одного из них. Поначалу магистры, архонты и старейшины купцов с удовольствием принимали последних Таргариенов в свои дома и к столам, 
           но годы шли, узурпатор продолжал восседать на Железном троне, и двери закрылись, заставив их жить скромнее. 
           Им пришлось продать последние оставшиеся драгоценности, а теперь закончились и деньги, которые они выручили за корону матери. 
           В переулках и питейных заведениях Пентоса ее брата звали королем-попрошайкой. Дэни не хотелось бы узнать, как они звали ее.
        </div>
        <img src="'''+ path +'''"><br>
    </body>
</html>''', 200, {
    'X-Daenerys Targaryen': 'Princess of Dragonstone',
    'X-Jon Snow': ' Lord Commander of the Nights Watch',
    'Content-Language': 'ru-RU'
    }

tree_planted = False

@app.route('/lab1/source')
def tree_status():
    style = url_for("static", filename="style2.css")
    path = url_for("static", filename="Дерево.jpg")
    global tree_planted
    status = "Дерево посажено" if tree_planted else "Дерево еще не посажено"
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>''' + status + '''</h1>
        <a href="/lab1/create">Посадить дерево</a><br>
        <a href="/lab1/delete">Полить дерево</a><br>
        <img src="'''+ path +'''">
    </body>
</html>
''', 200

@app.route('/lab1/create')
def plant_tree():
    style = url_for("static", filename="style2.css")
    path = url_for("static", filename="Посажено400.jpg")
    path1 = url_for("static", filename="Посажено201.jpeg")
    global tree_planted
    if tree_planted:
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
        <style>
            img {
                width: 65%;
            }
        </style>
    </head>
    <body>
        <p>Сначала полейте то, что посадили!</p>
        <a href="/lab1/source">Назад</a><br>
        <img src="'''+ path +'''">
    </body>
</html>
''', 400
    else:
        tree_planted = True
        return '''
<!doctype html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="''' + style + '''">
    <style>
        img {
            width: 60%;
        }
    </style>
</head>
    <body>
        <p>Ура! Дерево посажено, будем ухаживать :)</p>
        <a href="/lab1/source">Назад</a><br>
        <img src="'''+ path1 +'''">
    </body>
</html>
''', 201

@app.route('/lab1/delete')
def remove_tree():
    style = url_for("static", filename="style2.css")
    path = url_for("static", filename="Полито200.webp")
    path1 = url_for("static", filename="Полито400.webp")
    global tree_planted    
    if tree_planted:
        tree_planted = False
        return '''
<!doctype html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="''' + style + '''">
    <style>
        img {
            width: 60%;
        }
    </style>
</head>
    <body>
        <p>Дерево полито, можно сажать новое!</p>
        <a href="/lab1/source">Назад</a><br>
        <img src="'''+ path +'''"><br>
    </body>
</html>
''', 200
    else:
        return '''
<!doctype html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="''' + style + '''">
    <style>
        img {
            width: 60%;
        }
    </style>
</head>
    <body>
        <p>Не надо переливать его!!! Посадите лучше новое.</p>
        <a href="/lab1/source">Назад</a><br>
        <img src="'''+ path1 +'''"><br>
    </body>
</html>
''', 400
    
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
def add_flower():
    name = request.args.get('name')
    price = request.args.get('price')
    style = url_for("static", filename="main.css")
    if name and price:
        flower_list.append({'name': name, 'price': int(price)})
        flower_id = len(flower_list) - 1
        return redirect(url_for('flowers', flower_id=flower_id))
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