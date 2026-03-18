heart_rate = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
total = sum(heart_rate)
average = total / len(heart_rate)
print("There are", len(heart_rate), "patients in the dataset.")
print("The average heart rate is:", average)

low = 0
high = 0
normal = 0
for i in range(len(heart_rate)):
    if heart_rate[i] < 60:
        print("Patient", i+1, "has a low heart rate of", heart_rate[i], "bpm.")
        low += 1
    elif heart_rate[i] > 120:
        print("Patient", i+1, "has a high heart rate of", heart_rate[i], "bpm.")
        high += 1
    else:
        print("Patient", i+1, "has a normal heart rate of", heart_rate[i], "bpm.")
        normal += 1
if low > high and low > normal:
    print("Most patients have a low heart rate.")
elif high > normal:
    print("Most patients have a high heart rate.")
else:
    print("Most patients have a normal heart rate.")

import numpy as np
import matplotlib.pyplot as plt

plt.pie([low, normal, high], labels=['Low', 'Normal', 'High'], autopct='%1.1f%%', colors=['lightcoral', 'lightgreen', 'lightskyblue'])
plt.show()
