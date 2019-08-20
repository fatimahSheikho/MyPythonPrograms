array = ["Sara" , "Ghada", "Afnan","Ghalia", "Abeer"]
for x in array:
    if x == "Afnan" :
        continue
    elif x=="Ghalia":
        break
    print(x)

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)