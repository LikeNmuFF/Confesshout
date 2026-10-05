import os
import sqlite3
from flask import Blueprint, render_template, jsonify

display_bp = Blueprint("display", __name__, template_folder="../templates")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "db", "database.db")

@display_bp.route("/api/display")
def api_display():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT message, username, course, year_level, created_at
        FROM submission
        WHERE status = "approved" 
        AND created_at >= datetime('now', '-3 hours')
        ORDER BY created_at DESC
        '''
    )
    messages = cursor.fetchall()
    conn.close()
    display = [dict(zip(row.keys(), row)) for row in messages]
    return jsonify(display)



@display_bp.route("/display")
def display():
    return render_template('display.html')
