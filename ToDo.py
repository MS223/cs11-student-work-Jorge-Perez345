action = raw_input("What would you like to do?")
day = raw_input("What day?").capitalize()
days_of_the_week = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': [],
    'Sunday': [],
}
print days_of_the_week
def add():
    days_of_the_week[day] = action
print days_of_the_week
# im trying to figure out why the days in my dictionaries are not printing in order.
