word = "sun"
guess=""
guesslimit = 9
count =0
outlimit = False
while guess!=word  and not (outlimit):
    if count < guesslimit :
        guess = input("guess a word: ")
        count +=1
    else:
        outlimit = True
        print("You are out of guessing limit")
if guesslimit> count:
    print ("YOU WINNN!")