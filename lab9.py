from flask import Blueprint, render_template, request, session, redirect

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def lab():
    if request.method == 'POST':
        name = request.form.get('name')

        if name == '':
            return render_template('/lab9/lab9.html', error="Введите имя!")
        
        session['name'] = name
        return redirect('/lab9/age')
    
    return render_template('/lab9/lab9.html')


@lab9.route('/lab9/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        age = request.form.get('age')

        if age == '':
            return render_template('/lab9/age.html', error="Введите возраст!")
        
        session['age'] = age
        return redirect('/lab9/gender')
    
    return render_template('/lab9/age.html')


@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def gender():
    if request.method == 'POST':
        gender = request.form.get('gender')
        
        session['gender'] = gender
        return redirect('/lab9/preference')
    
    return render_template('/lab9/gender.html')


@lab9.route('/lab9/preference', methods=['GET', 'POST'])
def preference():
    if request.method == 'POST':
        preference = request.form.get('preference')
        
        session['preference'] = preference
        return redirect('/lab9/detail')
    
    return render_template('/lab9/preference.html')

@lab9.route('/lab9/detail', methods=['GET', 'POST'])
def detail():
    if request.method == 'POST':
        detail = request.form.get('detail')

        session['detail'] = detail
        return redirect('/lab9/congratulation')
    
    return render_template('/lab9/detail.html')

@lab9.route('/lab9/congratulation', methods=['GET'])
def congratulation():
    name = session.get('name')
    age = session.get('age')
    gender = session.get('gender')
    preference = session.get('preference')
    detail = session.get('detail')


    if gender == 'male':
        greeting = f"Поздравляю тебя, {name}!"
        if age.isdigit() and int(age) < 18:
            greeting += " Желаю, чтобы ты быстро вырос, был умным и всегда находил вдохновение в жизни!"
        else:
            greeting += " Желаю, чтобы ты был успешным, здоровым и счастливым!"
    else:
        greeting = f"Поздравляю тебя, {name}!"
        if age.isdigit() and int(age) < 18:
            greeting += " Желаю, чтобы ты быстро выросла, была умной и всегда находила вдохновение в жизни!"
        else:
            greeting += " Желаю, чтобы ты была успешной, здоровой и счастливой!"

    if preference == 'delicious':
        if detail == 'sweet':
            gift = "Вот тебе подарок — мнооого конфет!"
            image = "конфеты.png"
        else:
            gift = "Вот тебе подарок — вкуснейший новогодний кекс!"
            image = "пирог.png"
    else:
        if detail == 'beautiful':
            gift = "Вот тебе подарок — новогодний шар!"
            image = "шар.png"
        else:
            gift = "Вот тебе подарок — сюрприз под елкой!"
            image = "елка.png"

    return render_template('/lab9/congratulation.html', greeting=greeting, gift=gift, image=image)