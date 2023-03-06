import click
from spacetravel.db.models import Planet, Session
from spacetravel.travel import calculate_travel_time

session = Session()

@click.group()
def cli():
    pass

@cli.command()
def list():
    planets = session.query(Planet).all()

    for planet in planets:
        click.echo(f'{planet.name} ({planet.star_system}): {planet.distance} light-years from Earth')

@cli.command()
@click.argument('planet_name')
def info(planet_name):
    planet = session.query(Planet).filter_by(name=planet_name).first()

    if planet is None:
        click.echo(f'Planet {planet_name} not found')
    else:
        click.echo(f'Name: {planet.name}')
        click.echo(f'Star System: {planet.star_system}')
        click.echo(f'Distance from Earth: {planet.distance} light-years')

@cli.command()
@click.option('--system', help='Filter planets by the star system where they are located.')
@click.option('--distance', type=float, help='Filter planets by their distance from Earth in light-years.')
def filter(system, distance):
    if not system and not distance:
        click.echo('Please provide at least one filter option: --system or --distance')
        return

    if system:
        planets = session.query(Planet).filter_by(star_system=system).all()
    else:
        planets = session.query(Planet).filter(Planet.distance <= distance).all()

    if not planets:
        if system:
            click.echo(f'No planets found in the {system} star system')
        else:
            click.echo(f'No planets found within {distance} light-years from Earth')
        return

    for planet in planets:
        click.echo(f'{planet.name} ({planet.star_system}): {planet.distance} light-years from Earth')

@cli.command()
@click.argument('planet_name')
@click.option('--propulsion', type=click.Choice(['1', '2', '3'], case_sensitive=False),
              prompt='Please select a propulsion system [1: Ion Thruster, 2: Nuclear Pulse Propulsion, 3: Alcubierre Drive]:')
def travel(planet_name, propulsion):
    travel_time = calculate_travel_time(planet_name, propulsion)
    if travel_time == -1:
        click.echo('Invalid planet name or propulsion system')
    else:
        click.echo(f'Travel time to {planet_name}: {travel_time} years')

@cli.command()
def exit():
    click.echo('Goodbye!')
    raise SystemExit

if __name__ == '__main__':
    try:
        cli()
    except click.exceptions.Abort:
        click.echo('Operation aborted.')
    except Exception as e:
        click.echo(f'An error occurred: {e}')
