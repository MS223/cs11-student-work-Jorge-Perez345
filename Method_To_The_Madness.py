class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
    def __add__(self, other):
        return Time(self.hour + other.hour,self.minute + other.minute,self.second + other.second)
time1 = Time(1, 2, 3)
time2 = Time(4, 5, 6)
time3 = Time(7, 8, 9)
print time1
print time1 + time2
print time1 + time2 + time3
# I first created the class Time and I called hour, minute, and second with self. Then I created 3 different times and made them into an integer using str. 
# Finally I added each time and printed out the total of all 3 times.
