#for version
for x in range(1, 100):
    if x % 3 ==0:
        print(f"%d " % x, end = "")

print()
#while version
x = 1
while x < 101:
    #print(x)
    if x % 3 == 0:
        print(f"%d " % x, end = "")
    x += 1