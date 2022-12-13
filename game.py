'''Game "Guess the number"'''

'''Use the random function from the NumPy library, which will n\
    generate a random number from 1 to 100'''
import numpy as np
# guess a number
number = np.random.randint(1, 101) 
# install the counter
count = 0
while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("The number must be less!")

    elif predict_number < number:
        print("The number must be greater!")

    else:
        print(f"You guessed the number! This number = {number}, in {count} attempts")
        break # end game, exit loop