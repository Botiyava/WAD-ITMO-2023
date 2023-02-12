from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route("/")
def get_index():
    name = "Leo"
    deadline = datetime.datetime.strptime('2023/02/17', "%Y/%m/%d")
    time_before_deadline = deadline - datetime.datetime.utcnow().replace(microsecond=0)
#   a = {"utc": "1"}
#   return render_template("index.html", **a )
    return render_template("index.html",
                           name=name,
                           time_before_deadline=time_before_deadline)
