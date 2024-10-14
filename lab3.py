from flask import Blueprint, url_for, redirect, render_template, request, make_response
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age')

    if name is None:
        name = "Аноним"
    if age is None:
        age = "сколько-то"
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'rgb(167, 80, 80)')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')

    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


price = 0
@lab3.route('/lab3/pay')
def pay():
    global price
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10     
    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    global price 
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings/')
def settings():
    color = request.args.get('color')
    bgcolor = request.args.get('bgcolor')
    fsize = request.args.get('fsize')
    textalign = request.args.get('textalign')

    if color:
        resp = make_response(redirect('/lab3/settings/'))
        resp.set_cookie('color', color)
        return resp
    if bgcolor:
        resp = make_response(redirect('/lab3/settings/'))
        resp.set_cookie('bgcolor', bgcolor)
        return resp
    if fsize:
        resp = make_response(redirect('/lab3/settings/'))
        resp.set_cookie('fsize', fsize)
        return resp
    if textalign:
        resp = make_response(redirect('/lab3/settings/'))
        resp.set_cookie('textalign', textalign)
        return resp
    
    color = request.cookies.get('color')
    bgcolor = request.cookies.get('bgcolor')
    fsize = request.cookies.get('fsize')
    textalign = request.cookies.get('textalign')
    resp = make_response(render_template('lab3/settings.html', color=color, bgcolor=bgcolor, fsize=fsize, textalign=textalign))
    return resp

@lab3.route('/lab3/clear_cookie')
def clear_cookie():
    resp = make_response(redirect('/lab3/settings/'))
    resp.set_cookie('color', '')
    resp.set_cookie('bgcolor', '')
    resp.set_cookie('fsize', '')
    resp.set_cookie('textalign', '')
    return resp


@lab3.route('/lab3/form2/')
def form2():
    errors = {}
    pass_name = request.args.get('pass_name')
    if pass_name == '':
        errors['pass_name'] = 'Заполните поле!'

    shelf = request.args.get('shelf')
    bedding = request.args.get('bedding') == 'on'
    luggage = request.args.get('luggage') == 'on'
    
    age = request.args.get('age')
    if age == None:
        errors['age'] = ''
    elif age =='':
        errors['age'] = 'Заполните поле!'
    else:
        age = int(age)
        if age < 1 or age > 120:
            errors['age'] = 'Возраст должен быть от 1 до 120 лет!'

    departure = request.args.get('departure')
    if departure == '':
        errors['departure'] = 'Заполните поле!'

    destination = request.args.get('destination')
    if destination == '':
        errors['destination'] = 'Заполните поле!'

    date = request.args.get('date')
    if date == '':
        errors['date'] = 'Заполните поле!'
    
    insurance = request.args.get('insurance') == 'on'

    if 'age' in errors:
        price = 0
        ticket_type = ''
    else:
        if age >= 18:
            base_price = 1000
            ticket_type = 'Взрослый'
        else:
            base_price = 700
            ticket_type = 'Детский'

        if shelf in ['lower', 'lower_side']:
            base_price += 100
        if bedding:
            base_price += 75
        if luggage:
            base_price += 250
        if insurance:
            base_price += 150

        price = base_price

    return render_template('lab3/form2.html', errors=errors, pass_name=pass_name, shelf=shelf,
                           bedding=bedding, luggage=luggage, age=age, departure=departure,
                           destination=destination, date=date, insurance=insurance,
                           ticket_type=ticket_type, price=price)


products = [
    {"name": "Merci", "price": 449, "brand": "Storck", "flavor": "Ассорти"},
    {"name": "Raffaello", "price": 524, "brand": "Ferrero", "flavor": "Кокос"},
    {"name": "Snickers", "price": 112, "brand": "Mars", "flavor": "Арахис и карамель"},
    {"name": "Twix", "price": 112, "brand": "Mars", "flavor": "Карамель и печенье"},
    {"name": "Mars", "price": 112, "brand": "Mars", "flavor": "Карамель и нуга"},
    {"name": "Bounty", "price": 112, "brand": "Mars", "flavor": "Кокос"},
    {"name": "M&M's", "price": 224, "brand": "Mars", "flavor": "Шоколадные драже с начинкой"},
    {"name": "Kinder Chocolate", "price": 149, "brand": "Ferrero", "flavor": "Молочный шоколад"},
    {"name": "Milky Way", "price": 112, "brand": "Mars", "flavor": "Карамель и нуга"},
    {"name": "Kit Kat", "price": 112, "brand": "Nestle", "flavor": "Вафли с молочным шоколадом"},
    {"name": "Skittles", "price": 224, "brand": "Wrigley", "flavor": "Фруктовые конфеты"},
    {"name": "Haribo Goldbears", "price": 187, "brand": "Haribo", "flavor": "Желейные мишки"},
    {"name": "Chupa Chups", "price": 74, "brand": "Perfetti Van Melle", "flavor": "Леденцы на палочке"},
    {"name": "Mentos", "price": 149, "brand": "Perfetti Van Melle", "flavor": "Жевательные конфеты"},
    {"name": "Tic Tac", "price": 112, "brand": "Ferrero", "flavor": "Мятные леденцы"},
    {"name": "Alpenliebe", "price": 149, "brand": "Perfetti Van Melle", "flavor": "Молочный шоколад с начинкой"},
    {"name": "Ferrero Rocher", "price": 599, "brand": "Ferrero", "flavor": "Шоколадные конфеты с ореховой начинкой"},
    {"name": "Lindt Lindor", "price": 674, "brand": "Lindt", "flavor": "Шоколадные шарики с начинкой"},
    {"name": "Godiva", "price": 974, "brand": "Godiva", "flavor": "Премиальные шоколадные конфеты"},
    {"name": "Guylian", "price": 824, "brand": "Guylian", "flavor": "Шоколадные конфеты с морскими ракушками"},
]
@lab3.route('/lab3/search')
def search():
    return render_template('lab3/search.html')

@lab3.route('/lab3/result')
def result():
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    filtered_products = [
        product for product in products
        if (min_price is None or product['price'] >= min_price) and
           (max_price is None or product['price'] <= max_price)
    ]

    return render_template('lab3/result.html', products=filtered_products)