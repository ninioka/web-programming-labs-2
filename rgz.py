from flask import Blueprint, render_template, request, session, redirect, current_app, url_for
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path
import re
from flask import jsonify

rgz = Blueprint('rgz', __name__)

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='demchenko_rgz_knowledge_base',
            user='demchenko_rgz_knowledge_base',
            password='123'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database_rgz.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


VALID_USERNAME_PASSWORD_PATTERN = re.compile(r'^[a-zA-Z0-9\.\-_!@#$%^&*()+=?<>,;:"\'\[\]{}|~`]+$')


@rgz.route('/rgz/')
def rgr():
    if 'user_id' in session:
        return redirect('/rgz/dashboard')
    return render_template('/rgz/rgz.html')


@rgz.route('/rgz/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Проверка на пустые поля
        if not username or not password:
            return render_template('/rgz/register.html', error='Заполните все поля')

        # Проверка на валидность логина и пароля
        if not VALID_USERNAME_PASSWORD_PATTERN.match(username):
            return render_template('/rgz/register.html', error='Логин содержит недопустимые символы')
        if not VALID_USERNAME_PASSWORD_PATTERN.match(password):
            return render_template('/rgz/register.html', error='Пароль содержит недопустимые символы')

        conn, cur = db_connect()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()

        if user:
            return render_template('/rgz/register.html', error='Пользователь уже существует')

        hashed_password = generate_password_hash(password)
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id", (username, hashed_password))
        user_id = cur.fetchone()['id']
        conn.commit()
        db_close(conn, cur)

        # Автоматический вход после регистрации
        session['user_id'] = user_id
        session['username'] = username
        return redirect('/rgz/dashboard')

    return render_template('/rgz/register.html')


@rgz.route('/rgz/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return render_template('/rgz/login.html', error='Заполните все поля')

        conn, cur = db_connect()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()

        if not user or not check_password_hash(user['password'], password):
            return render_template('/rgz/login.html', error='Неверный логин или пароль')

        session['user_id'] = user['id']
        session['username'] = user['username']
        db_close(conn, cur)

        return redirect('/rgz/dashboard')

    return render_template('/rgz/login.html')


@rgz.route('/rgz/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/rgz/login')

    conn, cur = db_connect()
    cur.execute("SELECT * FROM users WHERE id != %s", (session['user_id'],))
    users = cur.fetchall()

    db_close(conn, cur)

    return render_template('/rgz/dashboard.html', users=users)


@rgz.route('/rgz/chat/<int:recipient_id>', methods=['GET', 'POST'])
def chat(recipient_id):
    if 'user_id' not in session:
        return redirect('/rgz/login')

    if request.method == 'POST':
        message_text = request.form['message_text']

        if not message_text:
            return redirect(url_for('rgz.chat', recipient_id=recipient_id))

        conn, cur = db_connect()
        cur.execute("INSERT INTO messages (sender_id, recipient_id, message_text) VALUES (%s, %s, %s)",
                    (session['user_id'], recipient_id, message_text))
        conn.commit()
        db_close(conn, cur)

        return redirect(url_for('rgz.chat', recipient_id=recipient_id))

    conn, cur = db_connect()
    cur.execute("""
        SELECT m.*, u.username AS sender_username
        FROM messages m
        JOIN users u ON m.sender_id = u.id
        WHERE (m.sender_id = %s AND m.recipient_id = %s) OR (m.sender_id = %s AND m.recipient_id = %s)
        ORDER BY m.id ASC
    """, (session['user_id'], recipient_id, recipient_id, session['user_id']))
    messages = cur.fetchall()

    cur.execute("SELECT id, username FROM users WHERE id = %s", (recipient_id,))
    recipient = cur.fetchone()

    db_close(conn, cur)

    return render_template('/rgz/chat.html', messages=messages, recipient=recipient)


@rgz.route('/rgz/delete_message/<int:message_id>', methods=['POST'])
def delete_message(message_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn, cur = db_connect()
    cur.execute("DELETE FROM messages WHERE id=%s AND (sender_id=%s OR recipient_id=%s)",
                (message_id, session['user_id'], session['user_id']))
    conn.commit()
    db_close(conn, cur)

    return redirect(request.referrer)


@rgz.route('/rgz/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect('/rgz/')


@rgz.route('/rgz/delete_account', methods=['POST'])
def delete_account():
    if 'user_id' not in session:
        return redirect('/rgz/login')

    conn, cur = db_connect()
    cur.execute("DELETE FROM users WHERE id=%s", (session['user_id'],))
    conn.commit()
    db_close(conn, cur)

    session.pop('user_id', None)
    session.pop('username', None)

    return redirect('/rgz/')


@rgz.route('/rgz/admin')
def admin():
    if 'user_id' not in session or session['username'] != 'admin':
        return redirect('/rgz/login')

    conn, cur = db_connect()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    db_close(conn, cur)

    return render_template('/rgz/admin.html', users=users)


@rgz.route('/rgz/admin/delete_user/<int:user_id>', methods=['POST'])
def admin_delete_user(user_id):
    if 'user_id' not in session or session['username'] != 'admin':
        return redirect('/rgz/login')

    conn, cur = db_connect()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    db_close(conn, cur)

    return redirect('/rgz/admin')


@rgz.route('/rgz/admin/edit_user/<int:user_id>', methods=['GET', 'POST'])
def admin_edit_user(user_id):
    if 'user_id' not in session or session['username'] != 'admin':
        return redirect('/rgz/login')

    conn, cur = db_connect()

    if request.method == 'POST':
        new_username = request.json.get('username')
        new_password = request.json.get('password')

        # Проверка на пустые поля
        if not new_username and not new_password:
            return jsonify({'success': False, 'error': 'Заполните хотя бы одно поле'}), 400

        # Проверка на валидность логина и пароля
        if new_username and not VALID_USERNAME_PASSWORD_PATTERN.match(new_username):
            return jsonify({'success': False, 'error': 'Логин содержит недопустимые символы'}), 400
        if new_password and not VALID_USERNAME_PASSWORD_PATTERN.match(new_password):
            return jsonify({'success': False, 'error': 'Пароль содержит недопустимые символы'}), 400

        if new_username:
            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute("UPDATE users SET username=%s WHERE id=%s", (new_username, user_id))
            else:
                cur.execute("UPDATE users SET username=? WHERE id=?", (new_username, user_id))
        if new_password:
            hashed_password = generate_password_hash(new_password)
            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute("UPDATE users SET password=%s WHERE id=%s", (hashed_password, user_id))
            else:
                cur.execute("UPDATE users SET password=? WHERE id=?", (hashed_password, user_id))

        conn.commit()
        db_close(conn, cur)
        return jsonify({'success': True})

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    else:
        cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cur.fetchone()
    db_close(conn, cur)

    return jsonify({
        'id': user['id'],
        'username': user['username']
    })