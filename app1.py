from flask import Flask
from flask import url_for,redirect

app = Flask(__name__) #create a WSGI application, coz its standard to communicate between client and server

@app.route('/') #decorator(rule,options). As soon as it goes to this url, this function will get triggered
def welcome():
    return "Welcome to flask tutorial, this is the demo tutorial to create a small skeleton"


@app.route('/success/<int:score>') #building URL dynamically
def success(score):
    return "The person has passed and the marks is " +str(score)

@app.route('/fail/<int:score>') #building URL dynamically
def fail(score):
    return "The person has failed and the marks is " +str(score)

#result checker
@app.route('/result/<int:marks>')
def reults(marks):
    result = ""
    if marks<50:
        result = "fail"
    else:
        result = "pass"

    return redirect(url_for(result,score = marks))





if __name__ == '__main__':
    app.run(debug = True)

