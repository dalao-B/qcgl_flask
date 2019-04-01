from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+mysqlconnector://root:123456@localhost/qcgl_flask",
                                    encoding='utf8', echo=True)

Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)


class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    cname = Column(String(20), nullable=False)
    cdetail = Column(String(50), nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)