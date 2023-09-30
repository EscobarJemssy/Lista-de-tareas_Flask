import mysql.connector

import click
from flask import current_app,g
from flask.cli import with_appcontext
from .schema import instructions_sql

def get_database():
    if 'mydatabase' not in g:
        g.mydatabase = mysql.connector.connect(
            host= current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        ) 
        g.cursor= g.mydatabase.cursor(dictionary=True)
        
    return g.mydatabase, g.cursor


def close_database(e=None):
    mydatabase = g.pop('mydatabase', None)
    
    if mydatabase is not None:
        mydatabase.close() #no activa la funcion
        
def init_database():
    mydatabase, cursor = get_database()
    
    for sql in instructions_sql:
        cursor.execute(sql)
    mydatabase.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_database()
    click.echo('Database initialized successfully')

def init_app(app):
    app.teardown_appcontext(close_database)
    app.cli.add_command(init_db_command)



