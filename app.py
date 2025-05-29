from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '最后一次提交到test'


if __name__ == '__main__':
    app.run()
