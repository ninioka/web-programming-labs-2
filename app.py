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