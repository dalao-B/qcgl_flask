from flask import Flask, redirect, request, render_template, make_response
import datetime
from orm import manage

app = Flask(__name__)

app.sened_file_max_age_default = datetime.timedelta(seconds=1)
app.debug =True

@app.route("/")
def index():
    user = request.cookies.get("username")
    return render_template("index.html", userinfo=user)


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        try:
            result = manage.checkUser(username, password)
            res = make_response(redirect("/list"))
            res.set_cookie("username",result,expires=datetime.datetime.now() + datetime.timedelta(days=7))
            return res
        except Exception as e:
            print(e)
            return redirect("/login")


@app.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method =="GET":
        return render_template("regist.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            manage.insetUser(username, password)
            return redirect("/login")
        except Exception as e:
            print(e)
            return redirect("/login")

@app.route("/quit")
def quit():
    res = make_response(redirect("/"))
    res.delete_cookie('username')
    return res


@app.route("/list")
def list():
    cars = manage.query_allcar()
    user = request.cookies.get("username")
    return render_template("list.html",cars=cars, user=user)


@app.route("/project/<int:id>")
def project(id):
    user = request.cookies.get("username")
    project = manage.query_project(id=id)
    return render_template("project.html", project=project, id=id,user=user)


@app.route("/addproject", methods=["GET","POST"])
def addproject():
    user = request.cookies.get("username")
    if request.method == "GET":
        return render_template("addproject.html",user=user)
    elif request.method == "POST":
        cname = request.form["cname"]
        cdetail = request.form["cdetail"]
        try:
            manage.insertCar(cname, cdetail)
            return redirect("/list")
        except Exception as e:
            print(e)
            redirect("/addproject")


@app.route("/delproject/<int:id>")
def delproject(id):
    manage.delCar(id=id)
    return redirect('/list')


@app.route("/updateproject/<int:id>", methods=["GET","POST"])
def updateproject(id):
    user = request.cookies.get("username")
    project = manage.query_project(id=id)
    if request.method == "GET":
        return render_template("updateproject.html",id=id,project=project,user=user)
    elif request.method == "POST":
        proname = request.form["cname"]
        procontent = request.form["cdetail"]
        try:
            manage.updateCar(proname, procontent,id=id)
            return redirect("/list")
        except Exception as e:
            print(e)
            redirect("/updateproject/{{id}}")




if __name__ == "__main__":
    app.run(port=8060)