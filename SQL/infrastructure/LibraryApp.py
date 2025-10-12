from infrastructure.mapper.AuthorMapper import AuthorMapper
from infrastructure.mapper.StatusMapper import StatusMapper
from infrastructure.mapper.BookMapper import BookMapper
from repositories.AuthorRepository import AuthorRepository
from repositories.BookRepository import BookRepository
from repositories.StatusRepository import StatusRepository
from services.LibraryService import LibraryService

class LibraryApp:
    def __init__(self, session):
        self.session = session
        self.books = BookRepository(session, BookMapper())
        self.authors = AuthorRepository(session, AuthorMapper())
        self.status = StatusRepository(session, StatusMapper) 
        self.library = LibraryService(library=self.books,authors=self.authors) 

    def initialize(self) -> None:
        self.library.add_by_str(book_title='Don Kichot', author_first_name='Miguel', author_last_name='de Cervantes')
        self.library.add_by_str(book_title='Opowieść o dwóch miastach', author_first_name='Charles', author_last_name='Dickens')
        self.library.add_by_str(book_title='Władca Pierścieni', author_first_name='John Ronald Reuel',
                        author_last_name='Tolkien')
        self.library.add_by_str(book_title='Mały Książę', author_first_name='Antoine', author_last_name='de Saint-Exupéry')
        self.library.add_by_str(book_title='Harry Potter i Kamień Filozoficzny', author_first_name='Joanne Kathleen',
                        author_last_name='Rowling')
        self.library.add_by_str(book_title='I nie było już nikogo', author_first_name='Agatha', author_last_name='Christie')
        self.library.add_by_str(book_title='Sen czerwonego pawilonu', author_first_name='Cao', author_last_name='Xueqin')
        self.library.add_by_str(book_title='Hobbit, czyli Tam i z powrotem', author_first_name='John Ronald Reuel',
                        author_last_name='Tolkien')
        self.library.add_by_str(book_title='She. Historia pewnej przygody', author_first_name='Henry Rider',
                        author_last_name='Haggard')
        self.library.add_by_str(book_title='Lew, czarownica i stara szafa', author_first_name='Clive Staples',
                        author_last_name='Lewis')
        self.library.add_by_str(book_title='Alicja w Krainie Czarów', author_first_name='Charles Lutwidge',
                        author_last_name='Dodgson')
        self.library.add_by_str(book_title='Przygody Pinokia', author_first_name='Carlo', author_last_name='Collodi')
        self.library.add_by_str(book_title='Kod Leonarda da Vinci', author_first_name='Dan', author_last_name='Brown')
        self.library.add_by_str(book_title='Harry Potter i Komnata Tajemnic', author_first_name='Joanne Kathleen',
                        author_last_name='Rowling')
        self.library.add_by_str(book_title='Harry Potter i Książę Półkrwi', author_first_name='Joanne Kathleen',
                        author_last_name='Rowling')
        self.library.add_by_str(book_title='Buszujący w zbożu', author_first_name='Jerome David', author_last_name='Salinger')
        self.library.add_by_str(book_title='Alchemik', author_first_name='Paulo', author_last_name='Coelho')
        self.library.add_by_str(book_title='Harry Potter i więzień Azkabanu', author_first_name='Joanne Kathleen',
                        author_last_name='Rowling')
        self.library.add_by_str(book_title='Harry Potter i Czara Ognia', author_first_name='Joanne Kathleen',
                        author_last_name='Rowling')
        self.library.add_by_str(book_title='Harry Potter i Zakon Feniksa', author_first_name='Joanne Kathleen',
                        author_last_name='Rowling')
        self.library.add_by_str(book_title='Harry Potter i Insygnia Śmierci', author_first_name='Joanne Kathleen',
                        author_last_name='Rowling')
        self.library.add_by_str(book_title='Mosty Madison', author_first_name='Robert James', author_last_name='Waller')
        self.library.add_by_str(book_title='Ben-Hur: Opowieść o Chrystusie', author_first_name='Lewis',
                        author_last_name='Wallace')
        self.library.add_by_str(book_title='Możesz uzdrowić swoje życie', author_first_name='Louise', author_last_name='Hay')
        self.library.add_by_str(book_title='Sto lat samotności', author_first_name='Gabriel García', author_last_name='Márquez')
        self.library.add_by_str(book_title='Lolita', author_first_name='Vladimir', author_last_name='Nabokov')
        self.library.add_by_str(book_title='Heidi', author_first_name='Johanna', author_last_name='Spyri')
        self.library.add_by_str(book_title='Pajączek Charlotty', author_first_name='Elwyn Brooks', author_last_name='White')
        self.library.add_by_str(book_title='Czarne piękno', author_first_name='Anna', author_last_name='Sewell')
        self.library.add_by_str(book_title='Myśl i bogać się', author_first_name='Napoleon', author_last_name='Hill')
        self.library.add_by_str(book_title='Zdrowie i opieka nad maluchem', author_first_name='Benjamin',
                        author_last_name='Spock')
        self.library.add_by_str(book_title='Ania z Zielonego Wzgórza', author_first_name='Lucy Maud',
                        author_last_name='Montgomery')
        self.library.add_by_str(book_title='Zabić drozda', author_first_name='Nelle Harper', author_last_name='Lee')
        self.library.add_by_str(book_title='Duma i uprzedzenie', author_first_name='Jane', author_last_name='Austen')
        self.library.add_by_str(book_title='Chłopiec w pasiastej piżamie', author_first_name='John', author_last_name='Boyne')
        self.library.add_by_str(book_title='Przygody Tomka Sawyera', author_first_name='Samuel Langhorne',
                        author_last_name='Clemens')
        self.library.add_by_str(book_title='Wybór Zofii', author_first_name='William', author_last_name='Styron')
        self.library.add_by_str(book_title='Pięć języków miłości', author_first_name='Gary', author_last_name='Chapman')
        self.library.add_by_str(book_title='Mężczyźni, którzy nienawidzą kobiet', author_first_name='Stieg',
                        author_last_name='Larsson')
        self.library.add_by_str(book_title='Zmierzch', author_first_name='Stephenie', author_last_name='Meyer')
        self.library.add_by_str(book_title='Igrzyska śmierci', author_first_name='Suzanne', author_last_name='Collins')
        self.library.add_by_str(book_title='Dziennik Anny Frank', author_first_name='Annelies Marie', author_last_name='Frank')
        self.library.add_by_str(book_title='Dzieci z Bullerbyn', author_first_name='Astrid', author_last_name='Lindgren')
        self.library.add_by_str(book_title='Chata', author_first_name='William Paul', author_last_name='Young')
        self.library.add_by_str(book_title='Na Zachodzie bez zmian', author_first_name='Erich Maria',
                        author_last_name='Remarque')
        self.library.add_by_str(book_title='Bieguni', author_first_name='Olga', author_last_name='Tokarczuk')
        self.library.add_by_str(book_title='Pachnidło: Historia pewnego mordercy', author_first_name='Patrick',
                        author_last_name='Süskind')
        self.library.add_by_str(book_title='Rok 1984', author_first_name='Eric Arthur', author_last_name='Blair')
        self.library.add_by_str(book_title='451° Fahrenheita', author_first_name='Ray', author_last_name='Bradbury')
        self.library.add_by_str(book_title='Chłopiec z latawcem', author_first_name='Khaled', author_last_name='Hosseini')


