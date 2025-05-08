from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app1 = Flask(__name__)
app1.config['SECRET_KEY'] = 'blahblahblah'
app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app1)
from routes import *

if __name__ == '__main__':
    app1.run(debug=True)
