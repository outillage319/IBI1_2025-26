import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

os.chdir("C:\\Users\\黄崇严\\OneDrive - International Campus, Zhejiang University\\文档\\IBI\\Week10")

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

first_10_rows = dalys_data.iloc[0:10, [2, 3]]
print("The third and fourth columns of the first 10 rows are:")
print(first_10_rows)

afghanistan_data = dalys_data.loc[dalys_data["Entity"] == "Afghanistan"]
afg_10_rows = afghanistan_data.head(10)
afg_max_year = afg_10_rows.loc[afg_10_rows["DALYs"].idxmax(), "Year"]
print("The max DaLYs year for Afghanistan in the first 10 rows is:", afg_max_year)
# The max DaLYs year for Afghanistan in the first 10 rows is: 1998

zimbabwe_data = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print("All years for Zimbabwe recording DALYs are:")
print(zimbabwe_data)
first_year_zimbabwe = zimbabwe_data.min()
last_year_zimbabwe = zimbabwe_data.max()
print("The first year for Zimbabwe recording DALYs is:", first_year_zimbabwe)
print("The last year for Zimbabwe recording DALYs is:", last_year_zimbabwe)
# The first year for Zimbabwe recording DALYs is: 1990
# The last year for Zimbabwe recording DALYs is: 2019

data_2019 = dalys_data.loc[dalys_data["Year"] == 2019]      
max_daly_2019_country = data_2019.loc[data_2019["DALYs"].idxmax(), "Entity"]
min_daly_2019_country = data_2019.loc[data_2019["DALYs"].idxmin(), "Entity"]
print("The country with the highest DALYs in 2019 is:", max_daly_2019_country)
print("The country with the lowest DALYs in 2019 is:", min_daly_2019_country)
# The country with the highest DALYs in 2019 is: Lesotho
# The country with the lowest DALYs in 2019 is: Singapore

target_country = max_daly_2019_country
target_data = dalys_data.loc[dalys_data["Entity"] == target_country]
plt.figure(figsize=(10, 6))
plt.plot(target_data["Year"], target_data["DALYs"], color="red", marker="o")
plt.title(f"DALYs over time for {target_country}")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.show()

# one other question: How has the DALYs rate in Zimbabwe changed compared to Afghanistan over the entire recorded period?
countries = ["Zimbabwe", "Afghanistan"]
comparison_data = dalys_data[dalys_data["Entity"].isin(countries)]
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = comparison_data[comparison_data["Entity"] == country]
    plt.plot(country_data["Year"], country_data["DALYs"], marker="o", label=country)
plt.title("DALYs trend for Zimbabwe and Afghanistan")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.legend()
plt.show()
print("The plot compares DALYs trends in Zimbabwe and Afghanistan from 1990 to 2019.")
print("Zimbabwe DALYs rose rapidly to a peak (2000~2004) then declined significantly.")
print("Afghanistan DALYs showed a consistent downward trend throughout the period.")