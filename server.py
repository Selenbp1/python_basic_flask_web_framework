from re import L
from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id':1,  'title': 'html', 'body': 'html is ...'},
    {'id':2,  'title': 'css', 'body': 'css is ...'},
    {'id':3,  'title': 'js', 'body': 'js is ...'},
]

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>Welcome</h2>
            Hello, Web
        </body>
    </html>
    '''

@app.route('/read/<int:id>/')
def read(id):
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    title = ''
    body = ''
    for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
    print(title,body)
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>({title}</h2>
            {body}
        </body>
    </html>
    '''

@app.route('/create/')
def create():
    return 'Create'




app.run(port=5001, debug=True)