from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
import os

admin_bp = Blueprint('admin', __name__, template_folder='../templates')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "db", "database.db")


def get_pending_messages():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT id, message, username, course, year_level, created_at
        FROM submission
        WHERE status = 'pending'
        ORDER BY created_at DESC
        '''
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


def check_admin(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT id, username, password, role
        FROM user
        WHERE username = ? AND password = ? AND role = "admin"
        ''',
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    return user is not None


@admin_bp.route('/admin/login', methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if check_admin(username, password):
            pending = get_pending_messages()
            return render_template('admin.html', message="Welcome Admin!", pending=pending)
        return render_template('login.html', message="Invalid credentials. Please try again.")
    return render_template('login.html')


@admin_bp.route('/admin/reject/<int:id>', methods=['POST'])
def reject_message(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM submission WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin.admin'))


@admin_bp.route('/admin/approve/<int:id>', methods=['POST'])
def approve_message(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE submission SET status = 'approved' WHERE id = ?",
        (id,)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('admin.admin'))


@admin_bp.route('/admin', methods=['GET'])
def admin():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, message, username, course, year_level, created_at
        FROM submission
        WHERE status = "pending"
        ORDER BY created_at DESC
    """)
    pending = cursor.fetchall()
    conn.close()
    return render_template('admin.html', pending=pending)