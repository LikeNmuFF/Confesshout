import os
import secrets

from dotenv import load_dotenv
from flask import Flask


load_dotenv()

app = Flask(__name__)
# Set SECRET_KEY in the environment for stable sessions across restarts and workers.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

# import routes
from routes.submit import submit_bp
from routes.display import display_bp
from routes.admin import admin_bp

app.register_blueprint(display_bp, url_prefix='')
app.register_blueprint(submit_bp, url_prefix='')
app.register_blueprint(admin_bp, url_prefix='')



if __name__ == "__main__":
    app.run(debug=True)