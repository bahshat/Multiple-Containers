from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String




app = Flask(__name__)

# create engine
engine = create_engine('postgresql://postgres:postgres@postgres-default:5432/postgres')

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

Base.metadata.create_all(engine)


@app.route('/')
def hello_world():
    print("Hello World")
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

