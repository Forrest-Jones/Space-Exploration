from sqlalchemy import create_engine, Column, Integer, String, Float, UniqueConstraint, CheckConstraint
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

    __table_args__ = (
        # Ensure that the planet name is unique
        UniqueConstraint('name', name='unique_planet_name'),
        # Ensure that the planet name, star system, and distance are not empty
        CheckConstraint('name != ""', name='non_empty_planet_name'),
        CheckConstraint('star_system != ""', name='non_empty_star_system'),
        CheckConstraint('distance > 0', name='positive_distance'),
    )
