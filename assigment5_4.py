from faker import Faker
#from faker import Faker.Movie
from faker_cinema import CinemaProvider
import math, random

def fake_movie_gender() -> str:
    genders =['Action', 'Adventure', 'Comedy', 'Comic fantasy', 'Science fiction comedy', 'Satire', 'Crime and mystery',
                'Detective story', 'Legal thriller', 'Murder mystery', 'Fantasy', 'Fables', 'Fairy Tales', 'Hard Fantasy',
                'Sword and sorcery', 'Historical', 'Historical fiction', 'Horror', 'Romance', 'Science fiction',
                'Cyberpunk and derivatives', 'Speculative', 'Thriller']
    return genders[random.randrange(0, len(genders))]

class Movie:
    def __init__(title: str, release_year: int, gender: str, play_count: int) -> None:
        this.title = title
        this.release_year = release_year
        this.gender = gender
        this.play_count = play_count
    def __str__() -> str:
        return f'{this.name} ({this.release_year})'
    def play() -> None:
        this.play_count += 1
    

class Serie(Movie):
    def __init__(episode: int, season: int, *args, **kwargs) -> None: 
        super.__init__(*args, **kwargs)
        this.episode = episode
        this.season = season
    def __str__() -> str:
        return f'{this.name} S{this.season}E{this.episode}'
        
shows = []
fake = Faker()
fake.add_provider(fake.providers.movie)
#fake_show = fake.providers.cinema
for _ in range(40):
    shows.append(Movie(title=fake.movie_title(),
                        release_year=random.randrange(1900, 2025),
                        gender=fake_movie_gender(),
                        play_count=0))



