import numpy as np
import matplotlib.pyplot as plt

N = 10000           
beta = 0.3          
gamma = 0.05       
time_steps = 1000   

S = N - 1
I = 1
R = 0

S_array = [S]
I_array = [I]
R_array = [R]

for t in range(time_steps):
    
    infection_prob = beta * (I / N)
    
    new_infections = np.random.choice(
        [0, 1], 
        size=S, 
        p=[1 - infection_prob, infection_prob]
    )
    
    num_new_infected = np.sum(new_infections)
    
    recoveries = np.random.choice(
        [0, 1], 
        size=I, 
        p=[1 - gamma, gamma]
    )
    num_new_recovered = np.sum(recoveries)
    
    S = S - num_new_infected
    I = I + num_new_infected - num_new_recovered
    R = R + num_new_recovered
    
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

plt.figure(figsize=(6, 4), dpi=150)

plt.plot(S_array, label='susceptible', color='steelblue', linewidth=1.5)
plt.plot(I_array, label='infected', color='darkorange', linewidth=1.5)
plt.plot(R_array, label='recovered', color='forestgreen', linewidth=1.5)

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.tight_layout()
plt.show()