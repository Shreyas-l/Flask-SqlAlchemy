from flask import Flask
from flask_mail import Mail,Message
import psycopg2
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:shreyasfcrit@23.236.50.224:5432/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



from WebApp import routes

