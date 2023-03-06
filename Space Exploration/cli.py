import click
from spacetravel.db.models import Planet, Session

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

if __name__ == '__main__':
    cli()
