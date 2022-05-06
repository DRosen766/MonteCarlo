from MonteCarlo.SpinConfiguration import *

"""
Module containing the SingleDimensionHamiltonian class
"""


class SingleDimensionHamiltonian:

    """Class for Single Dimension Hamiltonian\n
        NOTE: k constant is set to one
        
        :param J: a constant that determines the energy scale
        :param mu: a constant that represents the magnetic moment of the system
        :param spinConfiguration: the spin configuration of the system
        :type spinConfiguration: spinConfiguration
    """
#     k constant, arbitrarily sent to 1
    
#     constructor
    def __init__(self, J, mu, spinConfiguration):
        """Constructor function for class
        """
        self.k = 1
        self.J = J
        self.mu = mu
        self.spinConfiguration = spinConfiguration
        self.Hamiltonian = self.calculateHamiltonian()
        
    def calculateHamiltonian(self):
        """Helper function to calculate Ising hamiltonian value of spinConfiguration attribute using 

            .. math:: 
                \\hat{H}'=\\frac{\hat{H}}{k} = -\\frac{J}{k}\sum_{<ij>} s_is_j

            where, $$s_i=1$$ if the $$i^{th}$$ spin is `up` and $$s_i=-1$$ if it is `down`
            
            :return: Ising Hamiltonian Value of given spin configuration
            :rtype: float
        """
        factor = -1 * self.J / self.k
        spinSums = 0
#         nested loops calculate alignment factor for each pair of elements
        for i in range(0, self.spinConfiguration.getNumElements()):
            for j in range(0, self.spinConfiguration.getNumElements()):
                if(i != j):
                    spinSums += self.spinConfiguration.spins[i] * self.spinConfiguration.spins[j]
        return factor * spinSums
                    
        
    def calculateEnergy(self):
        """Calculates the energy of this system using:

            .. math::
                E = -J\sum_{ij} \sigma_i\sigma_j - \mu\sum_{j}\sigma_j

        """
        sumOfProductsOfSpins = 0
        sumOfSpins = 0
        for i in range(self.spinConfiguration.numElements):
            sumOfSpins += self.spinConfiguration.spins[i]
            for j in range(1, self.spinConfiguration.numElements):
                if(i + 1 == j):
                    sumOfProductsOfSpins += self.spinConfiguration.spins[i] * self.spinConfiguration.spins[j]
        sumOfProductsOfSpins += self.spinConfiguration.spins[0] * self.spinConfiguration.spins[self.spinConfiguration.numElements - 1]
        firstComponent = -1 * self.J * sumOfProductsOfSpins
        secondComponent = self.mu * sumOfSpins
        
        
        instanceEnergy = firstComponent + secondComponent
        return instanceEnergy
