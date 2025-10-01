from faker import Faker

class BaseContact:
    def __init__(self, name: str, family_name: str, phone: str, email: str):
        self.name = name
        self.family_name = family_name
        self.phone = phone
        self.email = email
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

def create_contacts(count: int, contact_type='BaseContact' ) -> list[BaseContact]:
    fake = Faker()
    contacts = []
    if contact_type == 'BaseContact':
        for _ in range(count):
            contacts.append(BaseContact(
                name=fake.first_name(),
                family_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email()
            ))
    else:
        for _ in range(count):
            contacts.append(BusinessContact(
                position=fake.job(),
                company=fake.company(),
                business_phone=fake.phone_number(),
                email=fake.email(),
                name=fake.first_name(),
                family_name=fake.last_name(),
                phone=fake.phone_number()
            ))
    return contacts

if __name__ == '__main__':
    contacts = create_contacts(count=10)
    for contact in contacts: