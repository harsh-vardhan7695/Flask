### integrate html with flask
### http verb GET and POST

###jinja2 template engine

'''
{%...%} for statements
{{  }} expressions to print output 
'''
from flask import Flask
from flask import url_for,redirect,render_template,request

app = Flask(__name__) #create a WSGI application, coz its standard to communicate between client and server

@app.route('/') #decorator(rule,options). As soon as it goes to this url, this function will get triggered
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>') #building URL dynamically
def success(score):
    res = ""
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"
    exp = {'score':score,'res':res}
    return render_template('result.html',result=exp)


@app.route('/fail/<int:score>') #building URL dynamically
def fail(score):
    return render_template('result.html',result= score)


#result checker
@app.route('/result/<int:marks>')
def reults(marks):
    result = ""
    if marks<50:
        result = "fail"
    else:
        result = "pass"

    return redirect(url_for(result,score = marks))


###result checker html page
@app.route('/submit',methods = ['POST','GET'])
def submit():
    avg_total_score=0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        avg_total_score = (science+maths+c+datascience)/4

        res = ''
        if avg_total_score > 50:
            res = 'success'
        else:
            res = 'fail'

        return redirect(url_for(res,score = avg_total_score))

    




if __name__ == '__main__':
    app.run(debug = True)

