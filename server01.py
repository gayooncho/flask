from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    # 웹페이지에서 동적인 변화를 보임
    return str(random.random())

@app.route('/create')
def create():
    return 'Create'

# <>안에 이름을 정하면 그것을 받는 함수에 파라미터중에 같은 이름에 파라미터가 받을 수 있게 해줌 ?
@app.route('/read/<id>/')
def read(id):
    return 'Read 1'

# debug 모드는 실제 서비스에서 빼야함
app.run(debug= True)
