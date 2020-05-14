import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SERVER_NAME = 'localhost:5000'

# Connect to the database

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://Amira@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False