#Guess the secret number using while loop
secret_number=56
attempt=0
while True:             #for infinite loop
    guess=int(input("Guess the secret value: "))    
    attempt+=1            #For multiple time input
    if guess==secret_number:
        print("Congratulation! you successfully guessed the secret number")
        print(f"You passes in {attempt} attempts.")
        break
    else:
        print("You failed in guessing the secret number,try again")
