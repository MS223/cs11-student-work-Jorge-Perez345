name = raw_input("What's your name? ")#This first line asks the user for his/her name.
upper_bound = input("What's the biggest number you want to guess?")#This code asks for a big number.
import random#This code makes it possible to import a random number. 
random_number = random.randint(0, upper_bound)#This code picks a random number between 0 and the biggest number you chosed in line 2.
guess = input("What is your guess ")#This line is where the user begins to guess for the random number. 

while guess != random_number:#This is a loop that repeats if the user's guess doesn't equal the random number.
    if guess < random_number:
         print "The number is higher. Try again " + name#When the users guess is less than the random number it tell the user to try again.
    if guess > random_number:
        print "The number is lower. Try again " + name#When the users guess is greater than the random number it tells the user to try again.
    guess = input("What is your guess ")#This code repeats the loop. 

    if guess == random_number:#When the users get the right number is tell the user that he/she got it right. 
        print "YOU GOT IT RIGHT!"
        print "GOOD JOB " + name
