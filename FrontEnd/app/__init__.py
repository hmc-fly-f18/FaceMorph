import os
from config import Config
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename




app = Flask(__name__, static_url_path='')
app.config.from_object(Config)

from app import routes
