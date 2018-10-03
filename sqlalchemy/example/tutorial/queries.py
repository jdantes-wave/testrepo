from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie
from datetime import date

session = Session()

movies = session.query(Movie) \
    .filter(Movie.release_date > date(2015, 1, 1)) \
    .all()


print('Recent Movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')

the_rock_movies = session.query(Movie) \
    .join(Actor, Movie.actors) \
    .filter(Actor.name == 'Dwayne Johnson') \
    .all()

print('The Rock Movies:')
for movie in the_rock_movies:
    print(f'{movie.title} was released on {movie.release_date}')


glendale_stars = session.query(Actor) \
    .join(ContactDetails) \
    .filter(ContactDetails.address.ilike('%glendale%')) \
    .all()

print('Glendale:')
for actor in glendale_stars:
    print(f'{actor.name} in Glendale')
