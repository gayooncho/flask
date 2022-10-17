from random import random
from flask import Flask, request, redirect
import random

app = Flask(__name__)


nextId = 4
topics = [
    {'id' : 1, 'title' : 'html', 'body': 'html is ...'},
    {'id' : 2, 'title' : 'css', 'body': 'css is ...'},
    {'id' : 3, 'title' : 'javascript', 'body': 'javascript is ...'}
]

def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h2><a href = "/">WEB</a></h2>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href = "/create/">create</a></li>
            </ul>
        </body>
    </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href = "/read/{topic["id"]}/">{topic["title"]}</a></li>'

    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h3>WELCOME</h3> hello, WEB')

@app.route('/create/', methods = ['GET', 'POST'])
def create():

    if request.method == 'GET':
        content = '''

            <form action = "/create/" method = "POST">
                <p><input type = "text" name = 'title' placeholder = 'title'></p>
                <p><textarea name = 'body' placeholder = "body"></textarea></p>
                <p><input type = submit value = "create"></p>

            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        # 지금 쓰는 변수 nextId가 global 변수임을 선언해줌
        global nextId

        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, "title" : title, "body" : body}
        
        topics.append(newTopic)
        url = '/read/' + str(nextId) + "/"
        # 전역변수이기 때문에 위에서 선언
        nextId = nextId + 1
    return redirect(url)


@app.route('/read/<int:id>/')
def read(id):

    title = ''
    body = ''

    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    
    return template(getContents(), f'<h3>{title}</h3>{body}')

app.run(debug= True)