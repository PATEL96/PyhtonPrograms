with open("C:\RAJ\PyhtonPrograms\ClassWork\F2.txt", "r") as F1:
    data = F1.read().split()
    List = [data.count(i) for i in data]
    d = dict(zip(data, List))
    uniq = []
    for i in range(len(List)):
        if(List[i] == 1):
            uniq.append(data[i])
print("Unique Values: ", uniq)
print("Word Count: ", d)