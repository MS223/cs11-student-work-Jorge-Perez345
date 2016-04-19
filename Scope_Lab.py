a = [1, 2, 4]
b = a
# Updating the B will not affect A because B is not equal to nothing.

# input: a list of ints
# output: an int
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)
print my_list
# my_list will print out the updated list and it will print with the the number 4 replaced with "yo"

