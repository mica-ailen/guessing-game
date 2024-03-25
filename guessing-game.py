import random 

number = random.randint(2, 25)

print(number)

#print(number)

player_name = input("Hi, what's your name?")
number_of_guesses = 0

print("Super "+ player_name+ "! You are guessing a number between 2 and 25:")


while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses +=1

    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print("Your guess is too high")
    else:
        break

if guess == number:
    print("Congratulations, " + player_name + "! You guessed the number in " + str(number_of_guesses) + " tries!")
else:
    print("Sorry " + player_name + ", you did not guess the number")
