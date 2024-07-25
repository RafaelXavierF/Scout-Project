from flask import Blueprint, render_template

home = Blueprint(__name__, "home")

@home.route("/")
def homePage():
    return render_template("areaDeslogada.html")

@home.route("/cadastro")
def cadastroPage():
    return render_template("paginaCadastro.html")
