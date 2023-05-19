from flask import *

import joblib
app=Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/graph",methods=['post','get'])
def graph():
    return render_template("geaphview.html")

@app.route("/predict",methods=['post'])
def predict():
    v1=request.form['textfield']
    v2=request.form['textfield2']
    v3=request.form['textfield3']
    v4=request.form['textfield4']
    v5=request.form['textfield5']
    v6=request.form['textfield6']
    v7=request.form['textfield7']
    v8=request.form['select']
    v9=request.form['textfield8']
    row=[float(v1),
         float(v2),
         float(v3),
         float(v4),
         float(v5),
         float(v6),
         float(v7),
         float(v8),
         float(v9)]
    knn=joblib.load("knn-model.joblib")
    res=knn.predict([row])
    print(res,"++++++++++++++++++")
    if res[0]==0:
        return  render_template("result.html",val="Non-landslide")
    else:
        return render_template("result.html", val="Landslide")




app.run(debug=True)