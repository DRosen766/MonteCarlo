

class spinConfiguration:

    """Class for Spin Configuration

    :param binaryConfiguration: the binary representation of the spins of each component of the system where 0 is 'down' and 1 is 'up'
    :type binaryConfiguration: int
    :param numElements: number of components in system
    :type numElements: int
    """

    def __init__(self, binaryConfiguration, numElements):
        #     number of elements in list of spins
        self.binaryConfiguration = binaryConfiguration
        self.numElements = numElements
        self.spins = self.getSpins(binaryConfiguration)

    def getSpins(self, binaryConfiguration):
        """Helper function to convert the binaryConfiguration as an integer into a list of integers where 1 represents up and -1 represents down
            
            :rtype: List[int]
        """
        spinList = []
        bitList = [bit for bit in bin(binaryConfiguration)][2:self.numElements + 2]
        while(len(bitList) < self.numElements):
            bitList.insert(0, '0')

        for bitChar in bitList:
            if(bitChar == '0'):
                spinList.append(-1)
            else:
                spinList.append(1)
        return spinList

    def getNumElements(self):
        """:return: numberElements property of this spinConfiguration
        """
        return self.numElements

    def calculateMagnetism(self):
        """Calculates the magnetism of this spinConfiguration

        .. math:: 
            M(\\alpha) = N_{\\text{up}}(\\alpha) - N_{\\text{down}}(\\alpha)
        """
        magnetism = 0
        for i in range(self.numElements):
            magnetism += self.spins[i]
        return magnetism



        
