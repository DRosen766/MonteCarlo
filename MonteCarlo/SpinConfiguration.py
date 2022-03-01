class spinConfiguration:
    
        def __init__(self, binaryConfiguration, numElements):
#     number of elements in list of spins
            self.numElements = numElements
            self.spins = self.getSpins(binaryConfiguration)
            
        def getSpins(self, binaryConfiguration):
            spinList = []
            bitList = [bit for bit in bin(binaryConfiguration)][2:self.numElements + 2]
            while(len(bitList) < self.numElements):
                bitList.insert(0,'0')
            
            for bitChar in bitList:
                if(bitChar == '0'):
                    spinList.append(-1)
                else:
                    spinList.append(1)
            return spinList
        
        def getNumElements(self):
            return self.numElements
        
        def calculateMagnetism(self):
            magnetism = 0
            for i in range(self.numElements):
                magnetism += self.spins[i]
            return magnetism;
            