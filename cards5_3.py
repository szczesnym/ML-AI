from faker import Faker

class BaseContact:
    def __init__(self, name: str, family_name: str, phone: str, email: str):
        self.name = name
        self.family_name = family_name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f'Name:{self.name}, Surname:{self.family_name}, Phone:{self.phone}, E-mail:{self.email}'
    def contact(self) -> None:
        print(f'Wybieram numer {self.phone} i dzownię do {self.name} {self.family_name}')
    @property
    def label_length(self) -> str:
        return f'{len(self.name)} {len(self.family_name)}'

class BusinessContact(BaseContact):
    def __init__(self,
                 position: str,
                 company: str,
                 business_phone: str,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone
    def contact(self) -> None:
        print(f'Wybieram numer {self.business_phone} i dzownię do {self.name} {self.family_name}')
    def __str__(self):
        return super().__str__() + f' Position:{self.position}, Company:{self.company}, Business Phone:{self.business_phone}'

def create_contacts(count: int, contact_type='BaseContact' ) -> list[BaseContact]:
    fake = Faker()
    _contacts = []
    if contact_type == 'BaseContact':
        for _ in range(count):
            _contacts.append(BaseContact(
                name=fake.first_name(),
                family_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email()
            ))
    else:
        for _ in range(count):
            _contacts.append(BusinessContact(
                position=fake.job(),
                company=fake.company(),
                business_phone=fake.phone_number(),
                email=fake.email(),
                name=fake.first_name(),
                family_name=fake.last_name(),
                phone=fake.phone_number()
            ))
    return _contacts

if __name__ == '__main__':
    contacts = create_contacts(count=10, contact_type='BaseContact')
    for contact in contacts:
        print(contact)
        contact.contact()