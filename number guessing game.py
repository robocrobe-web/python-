#number guessing game 
import random 
while True: 
    correct_number = random.randint(1,100) 
    while True:

        guess = int(input("guess a number between 1 to 100: "))
        if guess == correct_number: 
                print('you won!')
                break 
        elif guess > correct_number: 
             print("too high")
        else: 
            print("too low")    

 
   
 

 