from flask import Flask, render_template, url_for, redirect
import datetime
import yaml


def get_footer_vars():
    with open('project_info/info.yaml', 'r') as file:
        footer_vars = yaml.safe_load(file)
    return footer_vars


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('get_profile'), 301)


@app.route('/profile')
def get_profile():
    vars = get_footer_vars()
    name = "Leo"
    deadline = datetime.datetime.strptime('2023/02/17', "%Y/%m/%d")
    time_before_deadline = deadline - datetime.datetime.utcnow().replace(microsecond=0)
#   a = {"utc": "1"}
#   return render_template("index.html", **a )
    return render_template("index.html",
                           name=name,
                           time_before_deadline=time_before_deadline,
                           version = vars['version'],
                           owner = vars['owner'])
