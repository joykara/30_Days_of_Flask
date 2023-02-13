import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SECRET_KEY: useful to generate signatures or tokens
    #value is an  expression with two terms, joined by the 'or'
    #first term, environment variable value
    #second term, is just a hardcoded string