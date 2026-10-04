from flask import Flask
#from dotenv import load_dotenv
#import os

#load_dotenv()

app = Flask(__name__)
#app.secret_key = os.getenv('SECRET_KEY', 'dev-key')


# import routes
from routes.submit import submit_bp
from routes.display import display_bp
from routes.admin import admin_bp
# Register blueprints of submit
#app.register_blueprint(submit.submit_bp, url_prefix='/')
#app.register_blueprint(admin.admin_bp, url_prefix='/admin')
#app.register_blueprint(api.api_bp, url_prefix='/api')

# Register blueprints of display
app.register_blueprint(display_bp, url_prefix='')

app.register_blueprint(submit_bp, url_prefix='')
#app.register_blueprint(display)
app.register_blueprint(admin_bp, url_prefix='')
#app.register_blueprint(api.bp)


if __name__ == "__main__":
    app.run(debug=True)