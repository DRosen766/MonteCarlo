class SingleDimensionHamiltionian:
#     k constant, arbitrarily sent to 1
    
#     constructor
    def __init__(self, J, mu, spinConfiguration):
        self.k = 1;
        self.J = J
        self.mu = mu
        self.spinConfiguration = spinConfiguration
        self.Hamiltonian = self.calculateHamiltonian()
        
    def calculateHamiltonian(self):
        factor = -1 * self.J / self.k
        spinSums = 0
#         nested loops calculate alignment factor for each pair of elements
        for i in range(0, self.spinConfiguration.getNumElements()):
            for j in range(0, self.spinConfiguration.getNumElements()):
                if(i != j):
                    spinSums += self.spinConfiguration.spins[i] * self.spinConfiguration.spins[j]
        return factor * spinSums
                    
        
    def calculateEnergy(self):
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
