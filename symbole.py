def check_palindron(candidate):
    #print(candidate)
    #print(len(candidate) // 2)
    for x in range(len(candidate) // 2):
        #print(x)
        if candidate[x] != candidate[len(candidate) -1 -x]:
            return False
    return True




symbol_array=[]
with open('symbole.txt', 'r') as file:
    for line in file:
        symbol_array.append(line.rstrip())
#print(symbol_array)
with open('symbole_result.txt', 'w+') as file:
    for symbol in symbol_array:
        if check_palindron(symbol):
            print(f'{symbol} palindron') 
            file.write(symbol + '\n')
           