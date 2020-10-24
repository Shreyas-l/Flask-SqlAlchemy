from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/salchemy'

db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'example'
	id = db.Column('id', db.Integer, primary_key = True)
	data = db.Column('data', db.Unicode) #VARCHAR

