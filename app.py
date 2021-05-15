from flask import Flask, render_template
import datetime

#init empty app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:name>")
def desc_pages(name):
    url = name+ ".html"
    return render_template(url,name = name)

#@app.route("/<string:name>")
#def hello_name(name):
#   return f"Hello {name}"

@app.route("/friday")
def friday():
    today = datetime.date.today().weekday()
    if today == 4:
        return render_template("friday.html", isFriday = "YES!!")
    else:
        return render_template("friday.html", isFriday = "No :(")

@app.route("/fridayv2")
def friday2():
    today = datetime.date.today().weekday()
    return render_template("friday2.html", today=today)

@app.route("/count")
def loop():
    #numbers = []
    #for number in range(0,5):
    #   numbers.append(number)
    return render_template("count.html")

@app.route("/fizzbuzz")
def fizzbuzz():
    return render_template("fizzbuzz.html")

