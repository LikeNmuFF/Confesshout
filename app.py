from flask import Flask


app = Flask(__name__)



# import routes
from routes.submit import submit_bp
from routes.display import display_bp
from routes.admin import admin_bp

app.register_blueprint(display_bp, url_prefix='')
app.register_blueprint(submit_bp, url_prefix='')
app.register_blueprint(admin_bp, url_prefix='')



if __name__ == "__main__":
    app.run(debug=True)