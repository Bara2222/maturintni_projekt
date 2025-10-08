from flask import render_template_string, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db
from models import User

# Jednoduché HTML šablony přímo ve stringu
register_html = """
<form method="POST">
  <input name="username" placeholder="Uživatelské jméno" required>
  <input name="password" type="password" placeholder="Heslo" required>
  <button type="submit">Registrovat</button>
</form>
"""

login_html = """
<form method="POST">
  <input name="username" placeholder="Uživatelské jméno" required>
  <input name="password" type="password" placeholder="Heslo" required>
  <button type="submit">Přihlásit</button>
</form>
"""

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"], method="sha256")

        if User.query.filter_by(username=username).first():
            flash("Uživatel už existuje!")
            return redirect(url_for("register"))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template_string(register_html)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("protected"))
        flash("Špatné jméno nebo heslo")
    return render_template_string(login_html)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/protected")
@login_required
def protected():
    return "Tajná stránka – jsi přihlášen!"
