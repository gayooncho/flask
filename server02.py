from random import random
from flask import Flask
import random

app = Flask(__name__)

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

@app.route('/create/')
def create():
    return 'Create'

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