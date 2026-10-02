from flask import Flask, Blueprint, render_template

submit_bp = Blueprint("submit", __name__, template_folder="../templates")

@submit_bp.route('/', methods=['GET', 'POST'])
@submit_bp.route('/api/submit', methods=["POST"])
@submit_bp.route('/form', methods=["GET", "POST"])
def form():
    return render_template('form.html')

