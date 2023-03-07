from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..lib.models import Base

engine = create_engine('sqlite:///spacetravel.db', echo=True)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)
