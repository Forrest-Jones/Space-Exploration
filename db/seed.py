import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from spacetravel.db.models import Planet

# Define a list of planets to seed the database with
default_planets = [
    {'name': 'Proxima Centauri b', 'star_system': 'Alpha Centauri', 'distance': 4.24},
    {'name': 'Kepler-442b', 'star_system': 'Lyra', 'distance': 1200},
    {'name': 'K2-18b', 'star_system': 'Lacerta', 'distance': 124},
    {'name': 'GJ 1061 d', 'star_system': 'Vela', 'distance': 12.9},
    {'name': 'Gliese 667 Cc', 'star_system': 'Scorpius', 'distance': 23.6},
    {'name': 'TRAPPIST-1e', 'star_system': 'Aquarius', 'distance': 40},
    {'name': 'LHS 1140b', 'star_system': 'Cetus', 'distance': 41.1}
]

def seed_db(planets=default_planets):
    # Connect to the database
    engine = create_engine('sqlite:///spacetravel.db')
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
        planets = default_planets

    # Seed the database with the specified dataset
    seed_db(planets=planets)
