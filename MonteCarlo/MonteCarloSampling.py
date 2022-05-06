from matplotlib import pyplot as plt
from MonteCarlo.Ising import calculateValues
from MonteCarlo.SpinConfiguration import *
from MonteCarlo.SingleDimensionHamiltonian import *
import math
import numpy as np






class MonteCarloSampling:
    """Class for Monte Carlo Sampling

    :param steps: number of samples that will be taken during the sweep
    :param sites: number of sites in Spin Configuration being samples
    :param J: a constant that determines the energy scale
    :param mu: a constant that represents the magnetic moment of the system
    :param temperature: temperature of the system
    """

    def __init__(self, steps, sites, J, mu, temperature, plot=False):
        # number of steps to calculate average
        self.steps = steps
        # number of sites in spin configuration
        self.sites = sites

        # define constants
        self.J = J
        self.mu = mu

        self.temperature = temperature

    def sweep(self):
        """Function for using random sampling to estimate the energy of a spin configuration
        """
        # instantiate values that will be used for this function
        currentSpinConfiguration = spinConfiguration(0, self.sites)
        oldHamiltonian = SingleDimensionHamiltonian(self.J, self.mu, currentSpinConfiguration)
        oldEnergy = oldHamiltonian.calculateEnergy()
        oldProbability = math.e ** ((-1 * oldEnergy) / self.temperature)
        averageEnergyNumerator = oldEnergy * oldProbability
        totalProbability = oldProbability
        averageEnergyList = []
        for _ in range(0, self.steps):
            randomBit = np.random.randint(self.sites)
            # flip random bit in spinConfiguration
            currentSpinConfigurationSpinList = currentSpinConfiguration.spins
            if(currentSpinConfigurationSpinList[randomBit] == -1):
                currentSpinConfigurationSpinList[randomBit] = 1
            else:
                currentSpinConfigurationSpinList[randomBit] = -1
            currentSpinConfiguration.spins = currentSpinConfigurationSpinList
            print(currentSpinConfiguration.spins)

            # currentBinaryConfiguration += 1 # this should flip a random bit, not increment the binary config
            newHamiltonian = SingleDimensionHamiltonian(self.J, self.mu, currentSpinConfiguration)
            newHamiltonianEnergy = newHamiltonian.calculateEnergy()
            energyDifference = newHamiltonianEnergy - oldEnergy
            newProbability = math.e ** ((-1 * newHamiltonianEnergy) / self.temperature)
            if(energyDifference >= 0):
                averageEnergyNumerator += newHamiltonianEnergy * newProbability
                totalProbability += newProbability
                originalHamiltonian = newHamiltonian
            else:
                # use a random number to determine if jump should occur
                probabilityDifference = newProbability / oldProbability

                if(np.random.rand() < probabilityDifference):
                    averageEnergyNumerator += newHamiltonianEnergy * newProbability
                    totalProbability += newProbability
                    originalHamiltonian = newHamiltonian
            averageEnergyList.append(averageEnergyNumerator / totalProbability)



        # py
        stepNums = [step for step in range(self.steps)]
        actualAverage = np.full(self.steps, calculateValues(self.temperature, self.J, self.mu, self.sites)["averageEnergy"])
        plt.plot(stepNums, actualAverage)
        plt.plot(stepNums, averageEnergyList)
        plt.show()

if __name__ == "__main__":
    mcSampling = MonteCarloSampling(30, 6, -1.1, 2, 10)
    mcSampling.sweep()