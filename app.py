from bottle import *
from bottle import Bottle, run

app = Bottle()

@route('/login')
def login():
    return '''
        <form action="/login" method="post">
        Username: <input name="username" type="text"/>
        Password: <input name="password" type="text"/>
        <input value="login" type="submit" />
        '''

@route('/login')
def do_log():
    username = request.form.get('username')
    password = request.form.get('password')
    return "<br> {} {} </br".format(username, password)

run(app, host='127.0.0.1', port=8080)
