import logging
import math

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def add(a: float, b: float, *args: float) -> float:
    logging.info(f'Dodaję: {a}, {b}, {', '.join(map(str, args[0]))}')
    return a + b + sum(args[0])


def sub(a: float, b: float) -> float:
    logging.info(f'odejmuję {b} or {a}')
    return a - b


def mul(a: float, b: float, *args: float) -> float:
    logging.info(f'Mnożę: {a}, {b}, {', '.join(map(str, args[0]))}')
    return a * b * math.prod(args[0])


def div(a: float, b: float) -> float | None:
    (logging.info(f'Dzielę {a} przez {b}'))
    if b != 0:
        return a / b
    else:
        logging.error('Dzielenie przez 0 jest niedozwolone')
        return None


operations = {'1': add,
              '2': sub,
              '3': mul,
              '4': div}


def define_operation() -> object:
    while True:
        action = input(
            'Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:')
        if action in operations.keys():
            return operations[action]
        else:
            logging.info(f'Podano {action} co nie jest symbolem działania')


def get_component(i: int) -> float:
    while True:
        fist_number = input(f'Podaj składnik {i} >')
        try:
            number = float(fist_number)
            return number
        except:
            logging.warning(f'Wprowadzono {fist_number}, co nie jest liczbą, spróbuj ponownie\n')


def get_additional_components(operation: object) -> list[float]:
    numbers = []
    print(f'Wybrałeś jako działanie {operation.__name__}, możesz podać dodatkowe składniki')
    counter = 1
    while True:
        next_number = input(f'Podaj składnik {counter + 2} lub jakikolwiek inny znak by zakończyć wprowadzanie >')
        try:
            numbers.append(float(next_number))
            counter += 1
        except:
            return numbers


if __name__ == '__main__':
    func = define_operation()
    a = get_component(1)
    b = get_component(2)
    additional_numbers = []
    if func.__name__ == 'add' or func.__name__ == 'mul':
        additional_numbers = get_additional_components(func)
        result = func(a, b, additional_numbers)
    else:
        result = func(a, b)

    if result is not None:
        print(f'Wynik to: %.4f' % result)
    else:
        logging.error(f'Błąd działań')
