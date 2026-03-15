#get users' data of age, weight and Cr
#judge user's gender and ensure corresponding coefficient k
#judge if age, weight, Cr and gender is illegal with "elif”
#bring the data into the formula and output the result
age = int (input("Please enter the age of the student in years: "))
weight = int (input("Please enter the weight of the student in kg: "))
Cr = float (input("Please enter your serum creatinine level (μmol/L): "))
gender = input("Please enter your gender (M/F): ") #get basic data
if gender == "M":
    k = 1  
else:
    k = 0.85 #determine coefficient related to gender
if age >= 100:
    print("The age of the student should be less than 100 years.")
elif weight <= 20 or weight >= 80:
    print("The weight of the student should be between 20 and 80 kg.")
elif Cr <= 0 or Cr >= 100:
    print("The serum creatinine level should be between 0 and 100 μmol/L.")
elif gender != "M" and gender != "F":
    print("The gender of the student should be either M or F.") #ensure whether basic data are within normal range
else:
    CrCl = ((140 - age) * weight * k) / (Cr * 72) #bring data into the formula
    print("The creatinine clearance of the student is:", CrCl)
    
