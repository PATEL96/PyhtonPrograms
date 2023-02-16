with open("C:\RAJ\PyhtonPrograms\ClassWork\F1.txt", "r") as F1, open("C:\RAJ\PyhtonPrograms\ClassWork\F2.txt", "w") as F2:
    data = F1.readlines()
    for i in range(len(data)):
        if(data[i] != '\n'):
            F2.write(data[i])
     