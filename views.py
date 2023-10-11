from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name = "Testing Name")

@views.route("/profile")
def profile():
    args = request.args
    return render_template("profile.html", name = args.get('name'))

@views.route("/json")
def get_getjson():
    args = request.args
    return jsonify({'name': args.get('name'), 'title': args.get('title')})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def redirect_home():
    return redirect(url_for("views.home"))