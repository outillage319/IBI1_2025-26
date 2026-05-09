import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000         
beta = 0.3
gamma = 0.05
time_steps = 1000

vaccination_rates = np.arange(0, 1.1, 0.1)  
plt.figure(figsize=(6, 4), dpi=150)

for i, vax_rate in enumerate(vaccination_rates):
    vaccinated = int(N * vax_rate)
    S = N - vaccinated - 1   
    I = 1
    R = vaccinated           
    
    I_array = [I]
    
    for t in range(time_steps):
        if S > 0 and I > 0:
            infection_prob = beta * (I / N)
            new_infections = np.random.choice(
                [0, 1], size=S, p=[1 - infection_prob, infection_prob]
            )
            num_new_infected = np.sum(new_infections)
        else:
            num_new_infected = 0
        
        if I > 0:
            recoveries = np.random.choice(
                [0, 1], size=I, p=[1 - gamma, gamma]
            )
            num_new_recovered = np.sum(recoveries)
        else:
            num_new_recovered = 0
        
        S = S - num_new_infected
        I = I + num_new_infected - num_new_recovered
        R = R + num_new_recovered
        
        I_array.append(I)
    
    color = cm.viridis(int(i * 255 / (len(vaccination_rates) - 1)))
    label = f'{int(vax_rate * 100)}%'
    plt.plot(I_array, color=color, label=label, linewidth=1.5)

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend(title='Vaccination rate', loc='upper right')
plt.tight_layout()

plt.show()