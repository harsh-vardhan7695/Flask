from flask import Flask

app = Flask(__name__) #create a WSGI application, coz its standard to communicate between client and server

@app.route('/') #decorator(rule,options). As soon as it goes to this url, this function will get triggered
def welcome():
    return "Welcome to flask tutorial, this is the demo tutorial to create a small skeleton"


@app.route('/secondfunction') #decorator(rule,options). As soon as it goes to this url, this function will get triggered
def second_fucntion():
    return "Welcome to flask tutorial, this is second function with different url passed in the decorator."

@app.route('/secondfunction/function_within_second') #decorator(rule,options). As soon as it goes to this url, this function will get triggered
def third_fucntion():
    return "Welcome to flask tutorial, this is third function within second function with different url passed in the decorator."


if __name__ == '__main__':
    app.run(debug = True)

