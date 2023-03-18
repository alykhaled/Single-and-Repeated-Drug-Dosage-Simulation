import numpy as np
import matplotlib.pyplot as plt

half_life = 3.2 # hours
plasma_volume = 3000 # mL
elimination_constant = -np.log(0.5)/half_life
t = np.arange(0, 8, 0.01)

aspirin_in_plasma = np.ones(shape=(800, 1))
aspirin_in_plasma[0] = 2*325*1000 # micrograms

elimination = elimination_constant*aspirin_in_plasma[0]
for i in range(1, 800):
    aspirin_in_plasma[i] = aspirin_in_plasma[0] * np.exp(-elimination_constant*t[i])

plasma_concentration = aspirin_in_plasma/plasma_volume

plt.plot(half_life, plasma_concentration[int(half_life*100)], 'o', color='red')
plt.plot([half_life, half_life], [0, plasma_concentration[int(half_life*100)]], color='red')
plt.plot([0, half_life], [plasma_concentration[int(half_life*100)], plasma_concentration[int(half_life*100)]], color='red')
plt.text(half_life, plasma_concentration[int(half_life*100)]+10, 'Half-life', color='red')

plt.plot(t, plasma_concentration)
plt.xlabel('Time (hours)')
plt.ylabel('Plasma Concentration (mg/L)')
plt.xlim(0, 8)
plt.ylim(0, 218)
plt.title('Single Dose')
plt.show()


