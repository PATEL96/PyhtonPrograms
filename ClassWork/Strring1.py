s = str(input("Enter Any Password: "))

c1 = 0
c2 = 0
c3 = 0

for i in s:
    if(i.isalpha()):
        c1 += 1
    elif(i.isnumeric()):
        c2 += 1
    else:
        c3 += 1

print(c1)
print(c2)
print(c3)
