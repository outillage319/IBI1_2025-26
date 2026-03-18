population2020 = {'UK':66.7, "China":1426, "Italy":59.4, "Brazil":208.6, "USA":331.6}
population2024 = {"UK":69.2, "China":1410, "Italy":58.9, "Brazil":212.0, "USA":340.1}
percentage_change = {}
for country in population2020:
    if country in population2024:
        change = ((population2024[country] - population2020[country]) / population2020[country]) * 100
        percentage_change[country] = change
        print(f"{country}: {change:.2f}% change in population from 2020 to 2024.")
sorted_countries = sorted(percentage_change, key=percentage_change.get, reverse=True)
print("Countries sorted by population growth rate: ", sorted_countries)
print("Country with the highest population growth rate: ", sorted_countries[0])
print("Country with the lowest population growth rate: ", sorted_countries[-1])
import numpy as np
import matplotlib.pyplot as plt
countries = list(percentage_change.keys())
growth_rates = list(percentage_change.values())
plt.bar(countries, growth_rates)
plt.xlabel("Countries")
plt.ylabel("Population Growth Rate (%)")
plt.title("Population Growth Rate by Country (2020-2024)")
plt.show()

