from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config()


from app import routes     #different URLs the application implements
