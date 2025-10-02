from faker import Faker
from faker.providers import BaseProvider

class MovieProvider(BaseProvider):
    def movie_title(self):
        return self.random_element([
            'The Grand Budapest Hotel',
            'Inception',
            'Parasite',
            'Mad Max: Fury Road',
            'Spirited Away'
        ])

# Initialize Faker and add the custom provider
fake = Faker()
fake.add_provider(MovieProvider)

# Generate a fake movie title
print(fake.movie_title())