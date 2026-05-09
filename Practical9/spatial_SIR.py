import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100), dtype=int)

outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Initial state (t=0)')
plt.colorbar(ticks=[0, 1, 2], label='State (0=S, 1=I, 2=R)')
plt.show()

beta = 0.3      
gamma = 0.05   

snapshots = {0: population.copy()}
time_points = [10, 50, 100]

for t in range(1, 101):
    infected_coords = np.where(population == 1)
    infected_list = list(zip(infected_coords[0], infected_coords[1]))
    
    new_infections = []
    
    for (i, j) in infected_list:
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue  
                
                ni, nj = i + di, j + dj
                
                if 0 <= ni < 100 and 0 <= nj < 100:
                    if population[ni, nj] == 0:
                        if np.random.random() < beta:
                            new_infections.append((ni, nj))
    
    for (ni, nj) in set(new_infections):
        population[ni, nj] = 1
    
    infected_coords = np.where(population == 1)
    infected_list = list(zip(infected_coords[0], infected_coords[1]))
    
    for (i, j) in infected_list:
        if np.random.random() < gamma:
            population[i, j] = 2  
    
    if t in time_points:
        snapshots[t] = population.copy()

fig, axes = plt.subplots(2, 2, figsize=(10, 10), dpi=150)

times = [0, 10, 50, 100]
for idx, t in enumerate(times):
    ax = axes[idx // 2, idx % 2]
    im = ax.imshow(snapshots[t], cmap='viridis', interpolation='nearest')
    ax.set_title(f't = {t}')
    if idx == 0:
        plt.colorbar(im, ax=ax, ticks=[0, 1, 2], 
                    label='0=Susceptible, 1=Infected, 2=Recovered')

plt.suptitle('Spatial SIR Model: Disease Spread Over Time', fontsize=14)
plt.tight_layout()
plt.show()