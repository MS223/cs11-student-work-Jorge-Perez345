a = 0
while a< 100:
	print a
"""
Prediction: I think that this funtion will print out all the numbers less than 100.
Observation: My prediction was wrong it printed infinity zeros instead.
 """
a = 0
while a < 100:
	a = a + 1
	print a
"""
Prediction: I think it will print all the numbers from 0-100 including 100.
Observation: My prediction was correct. It printed all the numbers starting from zero and ending with 100.
 """

a = raw_input("Would you like to quit: ")
while a != "y":
	a = raw_input("Would you like to quit: ")
"""
Prediction: I think the function will ask me if I would like to quit?
Observation: It prints 'Would you like to quit" and it keeps repeating when I say yes or no.
 """
