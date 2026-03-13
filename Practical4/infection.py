x = 5 #initial infected students
y = 0.4 #infection rate
i =1 #day number
while x <= 91:
    i += 1 #accumulated day number
    z = x * y #infected student number in the day
    x += z #accumulated infected student number
    print("The number of infected students in day " + str(i) + " is:", z)
else:
    print("The whole days are:", i)
