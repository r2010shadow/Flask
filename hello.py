from flask import Flask
app = Flask(__name__)

from flask.ext.script import Manager   # allow —-host -p
manager = Manager(app)

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')
   # return '<h1>hello my world!</h1>'

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
   #return '<h2>Hi , %s! see you there</h2>' % name


if __name__  == '__main__':
    manager.run()
    app.run(debug=True)
