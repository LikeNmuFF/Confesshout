from flask import Blueprint, render_template, request
import sqlite3
import os
submit_bp = Blueprint("submit", __name__, template_folder="../templates")
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "db", "database.db")
def submit_to_db(message, username, course, year_level):
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO submission (message, username, course, year_level, status) VALUES (?,?,?,?,?)
        ''',
        (message, username, course, year_level, "pending")
        
    )
    conn.commit()
    conn.close()


@submit_bp.route('/', methods=['GET', 'POST'])
@submit_bp.route('/api/submit', methods=["POST"])
@submit_bp.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        message = request.form.get("message")
        username = request.form.get("username")
        course = request.form.get("course")
        year_level = request.form.get("year_level")
        
        is_anonymous = request.form.get("anonymous")
        if is_anonymous == 'on':
            username = "Anonymous"
        if not message:
            return render_template("form.html", message="Message is required")
        submit_to_db(message, username, course, year_level)
        return render_template('form.html', message="The message is delivered!")
    return render_template('form.html')