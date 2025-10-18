from faker import Faker
from MovieProvider import MovieProvider
import random, datetime

class Movie:
    def __init__(self, title: str, release_year: int, gender: str, play_count=0) -> None:
        self.title = title
        self.release_year = release_year
        self.gender = gender
        self.play_count = play_count
    def __str__(self) -> str:
        return f'{self.title} ({self.release_year})'
    def __repr__(self) -> str:
        return f'{self.title} ({self.release_year} - {self.gender} - {self.play_count})'
    def play(self) -> None:
        self.play_count += 1
    

class Serie(Movie):
    def __init__(self, episode: int, season: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
    def __str__(self) -> str:
        return f'{self.title} S{self.season:02}E{self.episode:02}'
    def __repr__(self) -> str:
        return f'{super().__repr__()} , S{self.season}E{self.episode}'


def get_movies(movies: list[Movie]) -> list[Movie]:
    return [m for m in movies if isinstance(m, Movie) and not isinstance(m, Serie)]
def get_series(movies: list[Movie]) -> list[Movie]:
    return [m for m in movies if isinstance(m, Serie)]
def search(movies: list[Movie], title: str) -> list[Movie]:
    return [m for m in movies if title == m.title]
def search_like(movies: list[Movie], title: str) -> list[Movie]:
    return [m for m in movies if title in m.title]

def top_titles(movies: list[Movie], size: int, content_type="Movie" ) -> list[Movie]:
    if content_type == "Movie":
        return sorted(get_movies(movies), key=lambda m: m.play_count, reverse=True)[:size]
    else:
        return sorted(get_series(movies), key=lambda m: m.play_count, reverse=True)[:size]
    #return sorted([m for m in movies if isinstance(m, content_type)], key=lambda m: m.play_count, reverse=True)[:size]

def generate_view(movies: list[Movie]) -> None:
    random.choice(movies).play_count = random.randint(1, 100)

def generate_views(movies: list[Movie]) -> None:
    for _ in range(random.randint(1, 10)):
        generate_view(movies)

def generate_season(movies: list[Movie], series_title: str, release_year: int,
                     gender: str, season_no: int, no_of_episodes) -> list[Movie]:
    new_movies = movies.copy()
    for i in range(no_of_episodes):
        new_movies.append(Serie(title=series_title, release_year=release_year, gender=gender,
                                season=season_no, episode=i+1))
    return new_movies

def get_episode_count(series: list[Serie], title: str) -> int:
    return len(search(movies=series, title=title))
    #return sum(1 for t in series if t.title == title)


if __name__ == '__main__':
    print("Biblioteka filmów")
    shows = []
    fake = Faker()
    fake.add_provider(MovieProvider)
    for _ in range(40):
        shows.append(Movie(title=fake.movie_title(),
                            release_year=random.randrange(1900, 2025),
                            gender=fake.movie_gender()
                            ))
        shows.append(Serie(title=fake.movie_title(),
                           release_year=random.randrange(1900, 2025),
                           gender=fake.movie_gender(),
                           episode=random.randrange(1, 20),
                           season=random.randrange(1, 10)
                           ))
    generate_views(movies=shows)
    print(f'Najpopularniejsze filmy i seriale dnia %s'% datetime.datetime.now().strftime('%d.%m.%Y'))
    print(top_titles(movies=shows, size=3, content_type="Movie"))

#shows.append(Movie(title='Attack of Clones', release_year=2006, gender='SciFI'))
#search = search(title='Attack of Clones', movies=shows)
#print(search)
#for movie in get_movies(shows):
#    print(movie)

#for movie in get_series(shows):
#    print(movie)

#for item in search:
#    print(f'{repr(item)} {id(item)} {type(item)}')

#print(top_titles(movies=shows, size=10))
#new_shows = generate_season(shows, series_title='Clone Wars', release_year=2007, gender='SciFI', season_no=5, no_of_episodes=22)
#print(get_series(new_shows))
#series = get_series(new_shows)
#print(get_episode_count(series=series, title='Clone Wars'))