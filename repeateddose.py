import numpy as np
import matplotlib.pyplot as plt

half_life = 22 # hours
interval = 8 # hours
MEC = 10 # micrograms/mL
MTC = 20 # micrograms/mL
startTime = 0 # hours
volume = 3000 # mL
dosage = 100 * 1000 # micrograms
absorption_fraction = 0.12
elimination_constant = -np.log(0.5)/half_life
elimination = np.exp(-elimination_constant*interval)

drug_in_plasma = np.zeros(shape=(168, 1))
entering = dosage * absorption_fraction

t = np.arange(0, 168 )
change = 0
currentDose = 0
for i in range(0,168 ):
    if i % interval == 0:
        change = 0
        elimination = np.exp(-elimination_constant*interval)
        drug_in_plasma[i] = drug_in_plasma[currentDose] * elimination + entering
        currentDose = i
    else:
        change = change + 1
        elimination = np.exp(-elimination_constant*change)
        drug_in_plasma[i] = drug_in_plasma[currentDose] * elimination
plasma_concentration = drug_in_plasma / volume



plt.plot([0, 168], [MEC, MEC], color='green')
plt.plot([0, 168], [MTC, MTC], color='green')

plt.plot(t, plasma_concentration)
plt.xlabel('Time (hours)')
plt.ylabel('Plasma Concentration (mg/L)')
plt.xlim(0, 168)
plt.ylim(0,max(plasma_concentration.max(), MTC)+10) 
plt.title('Repeated Dose')
plt.show()
