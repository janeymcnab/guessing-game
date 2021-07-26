import random

print ("Guess a number between 1 and 100")


number = random.randint(1,100)

guess = int(input("Enter Your Guess: "))
print ("Your Guess is " + str(guess))
counter = 0

while (guess != number):
  counter += 1
  if counter == 5:
        print("Phew! This is taking a while!")
  if guess > number:
        guess = int(input("Too High! Try again: "))
  if guess < number:
        guess = int(input("Too Low! Try again: "))
  #guess = int(input("That's not it! Try again: "))



print("You got it!")
print("It took you " + str(counter) + " guesses!")
