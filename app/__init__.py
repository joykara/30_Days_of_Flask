from flask import Flask

app = Flask(__name__)

from app import routes     #different URLs the application implements
