from flask import Flask
from flask import url_for,redirect,render_template,request

app = Flask(__name__)

app = Flask(__name__) #create a WSGI application, coz its standard to communicate between client and server

@app.route('/') 
def welcome():
    return render_template('user.html')


@app.route('/success/<string:Applicant_Name>/<int:Applicant_Age>/<string:Applicant_contact>/<string:Applicant_email>/<string:CourseSelected>') #building URL dynamically
def success(Applicant_Name,Applicant_Age,Applicant_contact,Applicant_email,CourseSelected):
    res = ""
    #if Applicant_contact or Applicant_Name or Applicant_email or Applicant_Age or CourseSelected == 0:
    if Applicant_Name == "":
        res = 'Fill all the details'
    else:
        res = 'Form Submitted'
    exp = {'Applicant_Name':Applicant_Name,'Applicant_Age':Applicant_Age,'Applicant_contact':Applicant_contact,'Applicant_email':Applicant_email,'CourseSelected':CourseSelected}
    return render_template('submission.html',result=exp)


@app.route('/fail/<string:Applicant_Name>/<int:Applicant_Age>') #building URL dynamically
def fail(Applicant_Name):
    return render_template('submission.html',result= Applicant_Name)


#result checker
@app.route('/result/<string:Applicant_Name>')
def reults(Applicant_Name):
    result = ""
    if Applicant_Name == "":
        result = "fail"
    else:
        result = "pass"

    return redirect(url_for(result,name = Applicant_Name))


###result checker html page
@app.route('/submit',methods = ['POST','GET'])
def submit():
    Applicant_Name=""
    Applicant_Age = 0
    Applicant_email = ""
    Applicant_contact=""
    CourseSelected = ""

    if request.method == 'POST':
        name = str(request.form['name'])
        age = float(request.form['age'])
        email = str(request.form['email'])
        mobilenumber = str(request.form['mobilenumber'])
        course = str(request.form['course'])

        Applicant_Name = name
        Applicant_Age = age
        Applicant_email = email
        Applicant_contact = mobilenumber
        CourseSelected = course

        res = ''
        if Applicant_Name == "":
            res = 'fail'
        else:
            res = 'success'

        return redirect(url_for(res,Applicant_Name = Applicant_Name,Applicant_Age= Applicant_Age,Applicant_contact=Applicant_contact,Applicant_email=Applicant_email,CourseSelected=CourseSelected))

    

if __name__ == '__main__':
    app.run(debug = True)



