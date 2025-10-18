def check_palindron(candidate):
    for x in range(len(candidate) // 2):
        if candidate[x] != candidate[len(candidate) -1 -x]:
            return False
    return True

symbol_array=[]
with open('symbole.txt', 'r') as file:
    for line in file:
        symbol_array.append(line.rstrip())
with open('symbole_result.txt', 'w+') as file:
    for symbol in symbol_array:
        if check_palindron(symbol):
            print(f'{symbol} palindrom')
            file.write(symbol + '\n')
           