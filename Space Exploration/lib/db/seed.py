from spacetravel.db.models import Planet, Session

session = Session()

# Seed data for potentially habitable planets.
planets = [
    Planet(name='Proxima Centauri b', star_system='Alpha Centauri', distance=4.24),
    Planet(name='Kepler-442b', star_system='Lyra', distance=1200),
    Planet(name='K2-18b', star_system='Lacerta', distance=124),
    Planet(name='GJ 1061 d', star_system='Vela', distance=12.9),
    Planet(name='Gliese 667 Cc', star_system='Scorpius', distance=23.6),
    Planet(name='TRAPPIST-1e', star_system='Aquarius', distance=40),
    Planet(name='LHS 1140b', star_system='Cetus', distance=41.1)
]

for planet in planets:
    session.add(planet)

session.commit()
