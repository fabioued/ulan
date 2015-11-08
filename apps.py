from bottle import run, route, request, redirect
import aiml
from random import choice

botbrain = aiml.Kernel()
botbrain.learn('yulan.aiml')
exception_brainmatrix = ['\n','\t']
default_excuses = [':)',
                   'gatau :P',
                   ':3',
                   'ulan gatau, ajarin ulan dong',]

with open('yulan.aiml', 'r') as readbrain:
    brains = readbrain.readlines()

brain_matrix = []
for contents in brains:
    if contents not in exception_brainmatrix:
        brain_matrix.append(contents)

knowledge = '-'.join(brain_matrix)
questions = []

@route('/hello')
def VIEW():
    return '''
    <html>
    <title>ulan - aiml + python + bottle</title>
    <h1>Ulan</h1>
    <hr>
    <b> Ulan (baca: yu-lan) is a chatterbot based on yulanyulianty's answers on her ask.fm </b>
    <hr>
    <br></br>
    <p> you just asked {} </p>
    <form action="/login" method="post">
    ask: <input name="ask" type="text"/>
    <input value="tanya" type="submit" />
    <br></br>
    <p> status: </p>
    <p> current brain matrix: {} </p>
    <p> current AIML Brain knowledge(s)</p>
    <p> {} </p>
    </html>
    '''.format(questions,len(knowledge), knowledge)

@route('/ulan')
def ulanmain():
    pass


@route('/login', method='POST')
def AIML():
    ask = request.forms.get('ask')
    if ask != None or ask != "":
        questions.append(ask)
        try:
            ans = botbrain.respond(ask)
        except:
            ans = choice(default_excuses)
        ask_template = '<p> you just asked: {}'.format(ask)
        respond_template = '<p> her answer: {}'.format(ans)
        return ask_template, respond_template
        redirect('http://localhost:8080/hello')
    return "You asked nothing!"

run(host='localhost', port=8080, debug=True)
