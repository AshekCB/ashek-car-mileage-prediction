from flask import Flask,render_template,request
import model


app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    result=None
    if request.method=="POST":
        cyl=request.form['cylinders']
        dis=request.form['displacement']
        hp=request.form['horsepower']
        wt=request.form['weight']
        acc=request.form['acceleration']
        model_y=request.form['model_year']
        origin=request.form['origin']

        result=model.predict(cyl,dis,hp,wt,acc,model_y,origin)

        return render_template("home.html",result=result)
    else:
        return render_template("home.html",result=result)
    
if __name__=="__main__":
    app.run(debug=True)    
