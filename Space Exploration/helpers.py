from spacetravel.db.models import Planet, Session

session = Session()

def calculate_travel_time(planet_name, propulsion_type):
    planet = session.query(Planet).filter_by(name=planet_name).first()

    if planet is None:
        return -1

    if propulsion_type == '1':
        # Calculate travel time using Ion Thruster
        travel_time = planet.distance / 100000
    elif propulsion_type == '2':
        # Calculate travel time using Nuclear Pulse Propulsion
        travel_time = planet.distance / 10000
    elif propulsion_type == '3':
        # Calculate travel time using Alcubierre Drive
        travel_time = planet.distance / 10
    else:
        return -1

    return travel_time
