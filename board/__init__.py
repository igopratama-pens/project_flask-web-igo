import os
from dotenv import load_dotenv
from flask import Flask

from board import pages, posts, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

