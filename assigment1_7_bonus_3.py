x = 1
count = 1
while True:
    if x % 6 == 0:
        print(f"%d " % x, end="")
        count +=1
    if count > 30:
        break
    x +=1
