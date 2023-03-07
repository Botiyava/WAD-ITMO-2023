from flask import Flask, request, render_template, flash, redirect, url_for, session
from flask_pymongo import PyMongo
import datetime
import os
import yaml
from werkzeug.security import generate_password_hash, check_password_hash
application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
mongo = PyMongo(application)
application.secret_key = os.getenv("APP_SECRET_KEY")


def get_footer_vars():
    with open('project_info/info.yaml', 'r') as file:
        footer_vars = yaml.safe_load(file)
    return footer_vars


@application.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        try:
            mongo.db.flaskitems.insert_one({
                "_id": {"username": username},
                "password": generate_password_hash(password, method='sha256'),
                "email": email
            })
        except:
            flash('This username is already taken')
            return redirect(url_for('signup'))
        return redirect(url_for('signin'))
    return render_template('signup.html')


@application.route('/signin', methods=["POST", "GET"])
def signin():
    vars = get_footer_vars()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        resp = mongo.db.flaskitems.find_one({"_id": {"username": username}})
        if resp is None or not check_password_hash(resp['password'], password):
            flash('Login or password is incorrect')
            return redirect(url_for('signin'))
        session['username'] = request.form['username']
        return redirect(url_for('profile'))
    return render_template('signin.html',
                           version=vars['version'],
                           owner=vars['owner'])


@application.route('/')
def index():
    return redirect("/profile", 302)


@application.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signup'))


@application.route('/read/<username>')
def read(username):
    user = mongo.db.flaskitems.find_one({"username": username},
                                        {"password": 1})
    if user is None:
        return '''
    <h1>User doesn't exist</h1>
    '''
    return render_template('result.html', username=user["password"])


@application.route('/profile')
def profile():
    if 'username' in session:
        vars = get_footer_vars()
        name = "Leo"
        deadline = datetime.datetime.strptime('2023/02/17', "%Y/%m/%d")
        time_before_deadline = deadline - datetime.datetime.utcnow().replace(microsecond=0)
    #   a = {"utc": "1"}
    #   return render_template("index.html", **a )
        return render_template("profile.html",
                            name=name,
                            time_before_deadline=time_before_deadline,
                            version = vars['version'],
                            owner = vars['owner'])
    return redirect("/signin", 403)

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(
        host="0.0.0.0", port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
