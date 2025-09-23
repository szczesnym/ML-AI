import logging
import math
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

input_result = False
input_value = False
additional_numbers = True
numbers = []
while  not input_result:
    action = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:')
    try:
        int_action = int(action)
        if 0 < int_action < 5:
            input_result = True
        else:
            print(f'Podano {int_action} co nie jest symbolem działania')
    except:
        print('Nie podano liczby, spróbuj ponownie\n')

while not input_value:
    fist_number = input('Podaj składnik 1 >')
    try:
        numbers.append(float(fist_number))
        input_value = True
    except:
        print(f'Wprowadzono {fist_number}, co nie jest liczbą, spróbuj ponownie\n')
input_value = False
while not input_value:
    second_number = input('Podaj składnik 2 >')
    try:
        numbers.append(float(second_number))
        input_value = True
    except:
        print(f'Wprowadzono {second_number}, co nie jest liczbą, spróbuj ponownie\n')

if int_action == 1 or int_action == 3:
    more_numbers = input('Wybarane działa to dodawanie lub mnożenie czy chcesz podać wicej liczb - (t/n) ?')
    if more_numbers == 't':
        counter = 1
        while additional_numbers:
            next_number = input(f'Podaj składnik {counter + 2} lub jakikolwiek inny znak by zakończyć wprowadzanie >')
            try:
                numbers.append(float(next_number))
                counter += 1
            except:
                additional_numbers = False


match int_action:
    case 1:
        logging.info(f'Dodaję {numbers}')
        logging.info(f'Wynik to {sum(numbers)}')
    case 2:
        logging.info(f'Odejmuję {numbers[1]} od {numbers[0]}')
        logging.info(f'Wynik to {numbers[0] - numbers[1]}')
    case 3:
        logging.info(f'Mnoże {numbers}')
        logging.info(f'Wynik to {math.prod(numbers)}')
    case 4:
        if numbers[1] == 0:
            logging.error('Nie można dzielić przez ZERO')
        else:
            logging.info(f'Dzielę {numbers[0]} przez {numbers[1]}')
            logging.info(f'Wynik to {numbers[0] / numbers[1]}')
