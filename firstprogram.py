# SIMPLE MINI PROJECT OF PYTHON
import random
num = random.randint(1, 20)

while True:
    #GET GUESSING VALUE FROM USER
    given = input("Guess the Number Between 1 to 20 or QUIT (Q) =")

    #FOR QUIT
    if(given == "Q"):
        break

    #THREE POSSIBLITIES
    given = int(given)
    if(given < num):
        print("\nYour Number is samll, Guess Bigger")

    elif(given > num):
        print("\nYour Number is big, Guess Smaller")
    #WIN
    elif(given == num):
        print("\nCongratulations, This is Perfect Number")
        break
#RESULT
print("____Game Over____")