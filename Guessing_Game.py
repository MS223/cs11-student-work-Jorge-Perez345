name = raw_input("What's your name?")
upper_bound = input("What's the biggest number you want to guess?")
import random
random_number = random.randint(0, upper_bound)
if random_number < random_number:
    print "Your guess is too low"
    print random_number
