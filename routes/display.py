from flask import Flask, render_template, redirect, url_for, Blueprint


display_bp = Blueprint("display", __name__ , template_folder="../templates")
