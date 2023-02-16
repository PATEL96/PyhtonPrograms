with open("C:\RAJ\PyhtonPrograms\ClassWork\F2.txt", "r") as F1:
    data = F1.read().split()
    for i in data:
        if(i[-1] == 'n'):
            print(i)
print(data)