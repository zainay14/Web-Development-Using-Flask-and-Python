## Create a simple flask application

from flask import Flask,render_template,request,redirect,url_for

## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is "+str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)


## Assignemnt Try for loop

## Calculator
@app.route('/calculator', methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                result = num1 / num2

        except:
            result = "Error"

    return render_template("calculator.html", result=result)


if __name__=='__main__':
    app.run(debug=True)