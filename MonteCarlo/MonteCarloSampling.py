from matplotlib import pyplot as plt
from MonteCarlo.Ising import calculateValues
from SpinConfiguration import spinConfiguration
from SingleDimensionHamiltonian import SingleDimensionHamiltonian
import math
import numpy as np


# number of steps to calculate average
steps = 10
# define constants
J = -1
mu = 1.1
temperature = 1




n = 6 # number of sites
currentSpinConfiguration = spinConfiguration(0, n)
originalHamiltonian = SingleDimensionHamiltonian(J, mu, currentSpinConfiguration)
originalEnergy = originalHamiltonian.calculateEnergy()
originalProbability = math.e ** ((-1 * originalEnergy) / temperature)
averageEnergyNumerator = originalEnergy * originalProbability
totalProbability = originalProbability;
averageEnergyList = []

# def sweep():
for _ in range(0, steps):
    randomBit = np.random.randint(n)
    # flip random bit in spinConfiguration
    currentSpinConfigurationSpinList = currentSpinConfiguration.spins
    if(currentSpinConfigurationSpinList[randomBit] == -1):
        currentSpinConfigurationSpinList[randomBit] = 1
    else:
        currentSpinConfigurationSpinList[randomBit] = -1
    currentSpinConfiguration.spins = currentSpinConfigurationSpinList

    # currentBinaryConfiguration += 1 # this should flip a random bit, not increment the binary config
    newHamiltonian = SingleDimensionHamiltonian(J, mu, currentSpinConfiguration)
    newHamiltonianEnergy = newHamiltonian.calculateEnergy()
    energyDifference = newHamiltonianEnergy - originalEnergy
    newProbability = math.e ** ((-1 * newHamiltonianEnergy) / temperature)
    if(energyDifference >= 0):
        averageEnergyNumerator += newHamiltonianEnergy * newProbability
        totalProbability += newProbability
        originalHamiltonian = newHamiltonian
    else:
        # temporarily do nothing
        # should use a random number to determine if jump should occur
        probabilityDifference = newProbability / originalProbability

        if(np.random.rand() < probabilityDifference):
            averageEnergyNumerator += newHamiltonianEnergy * newProbability
            totalProbability += newProbability
            originalHamiltonian = newHamiltonian
    averageEnergyList.append(averageEnergyNumerator / totalProbability)



# for _ in range(steps):
#     sweep()



# py
stepNums = [step for step in range(steps)]
actualAverage = np.full(steps, calculateValues(temperature, J, mu, n)["averageEnergy"])
plt.plot(stepNums, actualAverage)
plt.plot(stepNums, averageEnergyList)
plt.show()
