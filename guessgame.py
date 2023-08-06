import random

def guess_game():
    data = random.randint(1, 3)
    attempts = 1

    def num_words(num):
        numAlpha  = {1: "one",
                     2:"two",
                     3:"three"}
        return numAlpha.get(num, str(num))

    while attempts <= 3 :
        guess_number = int(input("Enter Number! "))

        if guess_number == data:
            print("YOU WON on", num_words(attempts), "attempt(s)")
            break
        elif guess_number > data:
            print("HIGH GUESS!", data, "is Correct")
        else:
            print("LOW GUESS!", data, "is correct")

        attempts += 1
        if attempts <= 3:
            print(attempts, "attempt(s) left")
        else: 
            print("attempts finished TRY AGAIN!")
            break


guess_game()

                     

