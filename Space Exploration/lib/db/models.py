from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///spacetravel.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    star_system = Column(String(255), nullable=False)
    distance = Column(Float, nullable=False)
