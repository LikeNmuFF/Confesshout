from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, EqualTo
from init_db import user
import sqlite3

conn = sqlite3.connect("/db/confeshout.db")
cursor = conn.cursor()
