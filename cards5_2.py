from faker import Faker

class Card:
    def __init__(self, name: str, family_name: str,company: str, position: str) -> None:
        self.name = name
        self.family_name = family_name
        self.company = company
        self.position = position
        self.e_mail = f'{self.name.lower()}.{self.family_name.lower()}@example.com'
    def __str__(self) -> str:
        return f"{self.name} {self.family_name} {self.company} {self.position} {self.e_mail}"
    def __repr__(self) -> str:
        return f"Name:{self.name}, Family name:{self.family_name}, Company:{self.company}, Position:{self.position}, E-mail:{self.e_mail}\n"
    def contact(self) -> None:
        print(f'Kontaktuję się z {self.name} {self.family_name}, {self.position}, {self.e_mail}')
    @property
    def addressing(self) -> str:
        return f'{len(self.name)} {len(self.family_name)}'


if __name__ == "__main__":
    cards = []
    fake = Faker()
    for _ in range(5):
        cards.append(Card(name=fake.first_name(),
             family_name=fake.last_name(),
             company=fake.company(),
             position=fake.job()))
    #print(list_of_cards)
    for card in cards:
        print(f'{card.name} {card.family_name}, {card.e_mail}')
        print(card.addressing)
    print(f'By name sorted:\n{sorted(cards, key=lambda card: card.name)}')
    print(f'By family name sorted:\n{sorted(cards, key=lambda card: card.family_name)}')
    print(f'By e-mail sorted:\n{sorted(cards, key=lambda card: card.e_mail)}')