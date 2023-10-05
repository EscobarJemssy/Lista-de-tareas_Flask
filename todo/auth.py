import functools
from flask import (
    Blueprint, flash, g, render_template, request, url_for, session,redirect
    )
from werkzeug.security import check_password_hash, generate_password_hash
from todo.db import get_database


bp = Blueprint('auth', __name__, url_prefix='/auth')
@bp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        mydatabase, cursor = get_database()
        error=None
        cursor.execute(
            'select id_user from users where username = %s', (username,)
        )
        
        if not username:
            error='You have to enter a username.'
        elif not password:
            error='You have to enter a password'
        elif cursor.fetchone() is not None:
            error = f'El usuario {username} esta registrado'
            
        if error is None:
            cursor.execute(
                'insert into users(username,password) values (%s,%s)', (username, generate_password_hash(password))
                )
            mydatabase.commit()
            
            return redirect(url_for('auth.login')) 
        flash(error)

    return render_template('auth/register.html') 


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = get_database()
        error = None
        cursor.execute(
            'select * from users where username = %s', (username,)
        )
        user = cursor.fetchone()
        
        if (
            user is None
            or user is not None
            and not check_password_hash(user['password'], password)
        ):
            error = 'Usuario y/o contraseña invalida'
        if error is None:
            session.clear()
            session['user_id'] = user['id_user']
            return redirect(url_for('index')) #Falta crear función
        flash(error)

    return render_template("auth/login.html")
