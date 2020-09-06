import yahoo_fin.stock_info as si
from flask import Flask, render_template


app = Flask(__name__) # name for the Flask app (refer to output)

ticker = ['aapl', 'tsla', 'msft', 'sq']

stocks_dict={}

def render_dict(lst):
    for item in lst:
        stocks_dict[item]= str(round(si.get_live_price(item), 3))
    return stocks_dict

@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home():
    return render_template("home.html")

@app.route("/vishal", methods=['GET', 'POST', 'PUT']) # decorator
def vishal():
    s_dict = render_dict(ticker)
    return render_template("base.html", stocks_dict=s_dict)

@app.route("/pradeep", methods=['GET', 'POST', 'PUT']) # decorator
def pradeep():
    s_dict = render_dict(ticker)
    return render_template("base.html", stocks_dict=s_dict)

@app.route("/sunita", methods=['GET', 'POST', 'PUT']) # decorator
def sunita():
    s_dict = render_dict(ticker)
    return render_template("base.html", stocks_dict=s_dict)

app.run(use_reloader = True, debug=True)