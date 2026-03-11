x = 5
y = 0.4
i =1
while x <= 91:
    i += 1
    z = x * y
    x += z
    print("The number of infected students in " + str(i) + " days is:", z)
else:
    print("The whole days are:", i)