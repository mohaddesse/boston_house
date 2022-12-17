from flask import Flask,request,render_template,jsonify,url_for,redirect
import pandas as pd
import numpy as np
import pickle
import util
import sys
app=Flask(__name__)


@app.route("/home/",methods=["POST","GET"])
def predict_price_home():
    if request.method=="POST":
        data=[float(x) for x in request.form.values()]
        x=np.array(list(data)).reshape(1,-1)
        print(data,file=sys.stderr)
        #re=util.predict_price(x)
        response = jsonify({
            'estimated_price': util.predict_price(x)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return render_template("index.html",content="the predic price : {} .".format(util.predict_price(x)))
    else:
        return render_template("index.html")

@app.route("/<name>")
def back_to_home(name):
    return redirect(url_for("predict_price_home"))


@app.route("/predict_api",methods=["POST"])
def predict_api():
    data=request.json["data"] 
    x=np.array(list(data.values())).reshape(1,-1)
    response = jsonify({
            'estimated_price': util.predict_price(x)
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    



if __name__ == '__main__':
    util.load_data()
    app.run(debug=True)