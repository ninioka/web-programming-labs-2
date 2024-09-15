from flask import Flask, url_for, redirect
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
                <a href="/lab1/web">web</a>
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
    return redirect("/author")

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
    return "нет такой страницы", 404

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
            <a href = "/lab1">Первая лабораторная</a>
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
            <a href = '/'>Главная страница</a>
        </main>
        <footer>
            &copy; Нина Демченко, ФБИ-22, 3 курс, 2024
        </footer>
    </body>
</html>
'''