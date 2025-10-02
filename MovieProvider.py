from faker import Faker
from faker.providers import BaseProvider
import random

class MovieProvider(BaseProvider):
    def movie_title(self):
        imdb_top_150 = []
        with open('IMDb_Top_150.txt', 'r') as file:
            for line in file:
                #print(line.strip())
                imdb_top_150.append(line.strip())
        return random.choice(imdb_top_150)
    def movie_year(self) -> int:
        return random.randint(1905, 2020)
    def movie_gender(self) -> str:
        genders = ['Action', 'Adventure', 'Comedy', 'Comic fantasy', 'Science fiction comedy', 'Satire',
                   'Crime and mystery',
                   'Detective story', 'Legal thriller', 'Murder mystery', 'Fantasy', 'Fables', 'Fairy Tales',
                   'Hard Fantasy',
                   'Sword and sorcery', 'Historical', 'Historical fiction', 'Horror', 'Romance', 'Science fiction',
                   'Cyberpunk and derivatives', 'Speculative', 'Thriller']
        return genders[random.randrange(0, len(genders))]


# Initialize Faker and add the custom provider
#fake = Faker()
#fake.add_provider(MovieProvider)

# Generate a fake movie title
#print(fake.movie_title())