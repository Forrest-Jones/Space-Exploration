import argparse
import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.nasa_exoplanet import NasaExoplanet

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..lib.models import Base, Planet


# Define a list of planets to seed the database with
default_planets = [
    {'name': 'Kepler-438 b', 'star_system': 'Kepler-438', 'distance': 470},
    {'name': 'Kepler-442 b', 'star_system': 'Kepler-442', 'distance': 1200},
    {'name': 'Kepler-1229 b', 'star_system': 'Kepler-1229', 'distance': 770},
    {'name': 'Kepler-62 e', 'star_system': 'Kepler-62', 'distance': 1200},
    {'name': 'Kepler-62 f', 'star_system': 'Kepler-62', 'distance': 1200},
    {'name': 'Kepler-186 f', 'star_system': 'Kepler-186', 'distance': 490},
    {'name': 'Kepler-296 e', 'star_system': 'Kepler-296', 'distance': 990}
]

def get_planet_data():
    # Query the NASA Exoplanet Archive for potentially habitable planets
    exoplanets_table = NasaExoplanet.query_criteria(table='exoplanets',
                                                    where=f"pl_habitable='TRUE'")

    # Convert the query results to a list of dictionaries
    planet_data = []
    for row in exoplanets_table:
        planet_data.append({'name': row['pl_name'], 'star_system': row['pl_hostname'],
                            'distance': row['st_dist'] * u.parsec.to(u.lightyear)})
    return planet_data

def seed_db(planets=default_planets):
    # Connect to the database
    engine = create_engine('sqlite:///spacetravel.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Seed the database with planets
    for planet_data in planets:
        planet = Planet(**planet_data)
        session.add(planet)

    session.commit()

if __name__ == '__main__':
    # Add an argument to allow users to specify a custom dataset
    parser = argparse.ArgumentParser(description='Seed the database with planets')
    parser.add_argument('--dataset', nargs='*', help='a list of dictionaries containing planet data')
    args = parser.parse_args()

    # If the user specified a custom dataset, use that instead of the default
    if args.dataset:
        planets = args.dataset
    else:
        planets = get_planet_data()

    # Seed the database with the specified dataset
    seed_db(planets=planets)
