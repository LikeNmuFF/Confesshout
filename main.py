from flask import Flask, render_template, redirect, jsonify, url_for, request, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'your_secret_key'


par = 'Parageyan 2026'
conn = sqlite3.connect("db/confeshout.db")
cursor = conn.cursor()




@app.route('/')
def home():
    return render_template('index.html', par=par)

@app.route('/form', methods=["GET","POST"])
def form():
    return render_template('form.html')

@app.route('/api/submit', methods=["POST"])
def submit_form():
    data = request.json
    conn = sqlite3.connect(conn)
    cursor = conn.cursor()
    
    cursor.execute('''
                   INSERT INTO submission(message, username, course, status)
                   VALUES (?, ?, ?, ?)
                   ''', (data['message'], data['name'], data['course'], 'pending'))
    
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})



@app.route("/view")
def view_post():

    cursor.execute('''
                   SELECT id, message, username, course, created_at FROM submission WHERE status = "approved"
                   ''')
    posts = cursor.fetchall()

    post_lists = []
    for post in posts:
        post_lists.append({
            'id' : post[0],
            'message' : post[1],
            'name' : post[2],
            'course' : post[3],
            'created_at' : post[4]
            
        })
    
    
    conn.close()
    return render_template("view.html", post_lists=post_lists)

# Admin validation logics
@app.route("/admin", methods=["GET", "POST"])
def admin_login():

    
    cursor.execute('''
                   SELECT role FROM admin WHERE username = ? AND password = ?, (login-form.get("Username"), login-fomr.get("Password"))
                   
                   ''')
    admin = cursor.fetchone()
    conn.close()
    if admin is None:
        return "<h1 style=text-align:center;font-style:bold;>Unathorized access is prohibitted!!</h1>"
    elif admin['role'] != 'admin':
        return jsonify({"error": "Access Denied"}), 403
    
    return render_template("admin.html", welcome="Welcome Admin")
    

# delete data if it will last 3 hours
def delete_posts_3hrs():
    # post automatic delete if its equal to 3 hours:
    current_time = 'now'
    cursor.execute('''
                   SELECT * FROM submission WHERE created_at >= AND created_at <?
                   '''), (current_time, current_time)
    rows = cursor.fetchall()
    for row in rows:
        data = {
            'id': row[0],
            'created_at': row[1]
            
        }
        cursor.execute('DELETE * FROM submission where id ?', data['id'])
    
    
    

if __name__ == "__main__":
    app.run(debug=True)