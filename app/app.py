from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

# create engine
engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')

# create session
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Cars(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)    

Base.metadata.create_all(engine)


@app.route('/')
def hello_world():
    print("Hi Rais & Yameen!")
    return 'Now working. But is it from reload?'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

