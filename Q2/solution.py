file = input().split("\n")
temp = []
for i in file[1:len(file)]:
    temp.append(i.split())
allValid = "true"
errorCodes = []
for i in temp:
    allValid = i[1]
    if i[1] != "true":
        errorCodes.append(i[2])
if len(errorCodes) > 0:
    allValid = "false"
if allValid == "true":
    print("Yes")
else: print("No", ' '.join(errorCodes), sep="\n")