from orm import model
from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker

engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                                    encoding='utf8', echo=True)

session = sessionmaker()()


def insetUser(username, password):
    session.add(model.User(username=username, password=password))
    session.commit()
    session.close()


def checkUser(username, password):
    result = session.query(model.User).filter(model.User.username == username).filter(model.User.password==password).first().username
    if result:
        return result
    else:
        return -1



def query_allcar():
    allcar = session.query(model.Car.id,model.Car.cname,model.Car.cdetail).all()
    return allcar


def query_project(id):
    car= session.query(model.Car.cname,model.Car.cdetail).filter(model.Car.id == id).first()
    return car

def insertCar(cname, cdetail):
    session.add(model.Car(cname=cname, cdetail=cdetail))
    session.commit()
    session.close()

def delCar(id):
    session.query(model.Car).filter(model.Car.id == id).delete()
    session.commit()
    session.close()

def updateCar(cname, cdetail,id):
    session.query(model.Car).filter(model.Car.id == id).update({model.Car.cname:cname,model.Car.cdetail:cdetail})
    session.commit()
    session.close()