from flask import Blueprint, render_template, redirect, url_for, current_app

main_bp = Blueprint(
    'main_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/')
def home():
    return render_template("index.html")

