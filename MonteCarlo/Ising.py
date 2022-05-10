

# import classes
from MonteCarlo.SpinConfiguration import *
from MonteCarlo.SingleDimensionHamiltonian import *
import matplotlib.pyplot as plt
import math

# for now only produces the configurations with two elements, should change soon
def generateSpinConfigurations(n):
    """Calculates a list of all possible spin configurations with a given number of sites

    :param n: number of sites in each spin configuration
    :type n: int
    :rtype: List[spinConfiguration]
    """
    #generate spin configurations 
    spinConfigurations = []#convert each List in spinConfigurationsLists in SpinConfiguration object
    for binaryConfiguration in range(2 ** n):
        spinConfigurations.append(spinConfiguration(binaryConfiguration, n))

    return spinConfigurations


def calculateValues(temperature, J, mu, latticeLength):
    """calculates averageEnergy, averageMagnetism, HeatCapacity, and Magnetic Susceptibility

    :param temperature: temperature of system
    :param J: a constant that determines the energy scale
    :param mu: a constant that represents the magnetic moment of the system
    :param latticeLength: number of sites in spinConfigurations
    """
    #set k constant
    k = 1
    
    #instantiate probability variable
    totalProbability = 0

    #instantiate lists for Energies and Probabilities
    energies = []
    energiesSquared = []
    magnetisms = []
    magnetismsSquared = []
    probabilities = []
 
    #calculate spinConfiguration
    spinConfigurations = generateSpinConfigurations(latticeLength)
    
    #calculate Energies and Magnetisms for each spin configuration
    for i in range(len(spinConfigurations)):
#         define spinConfiguration and Hamiltonian for given instance
        instanceSpinConfiguration = spinConfigurations[i];
        instanceHamiltonian = SingleDimensionHamiltonian(J, mu, instanceSpinConfiguration)
        
#         add instance values to energies, magnetisms, and probabilities lists
        instanceEnergy = instanceHamiltonian.calculateEnergy()
        energies.append(instanceEnergy)
        instanceMagnetism = instanceSpinConfiguration.calculateMagnetism();
        magnetisms.append(instanceMagnetism)
        instanceProbability = math.e ** ((-1 * instanceEnergy) / temperature)
        probabilities.append(instanceProbability)
        
#         add instance probability to totalProbability
#         print("instanceProbability {}: {}".format(i, instanceProbability))
        totalProbability += instanceProbability
#     print("totalprobability: {}".format(totalProbability))
#     calculate Average Energy and Magnetism and EnergySquared and MagnetismSquared
    averageEnergyNumerator = 0
    averageEnergySquaredNumerator = 0
    averageMagnetismNumerator = 0
    averageMagnetismSquaredNumerator = 0
    
    
#     print(energies)
#     print(probabilities)
    for i in range(len(energies)):
#         print("instanceEnergy {}: {}".format(i, energies[i]))
#         print("instanceMagnetism {}: {}".format(i, magnetisms[i]))
        averageEnergyNumerator += energies[i] * probabilities[i]
        averageEnergySquaredNumerator += energies[i] * energies[i] * probabilities[i]
        averageMagnetismNumerator += magnetisms[i] * probabilities[i]
        averageMagnetismSquaredNumerator += magnetisms[i] * magnetisms[i] * probabilities[i]
    
#     print("averageEnergyNumerator: {}".format(averageEnergyNumerator))
    averageEnergy = averageEnergyNumerator / totalProbability
    averageEnergySquared = averageEnergySquaredNumerator / totalProbability
    averageMagnetism = averageMagnetismNumerator / totalProbability
    averageMagnetismSquared = averageMagnetismSquaredNumerator / totalProbability

    # return results as a dictionary
    return {"averageEnergy": averageEnergy, 
            "averageEnergySquared": averageEnergySquared,
            "averageMagnetism": averageMagnetism,
            "averageMagnetismSquared": averageMagnetismSquared,
            "temperature": temperature,
            "partition": totalProbability
           }



def calculateHeatCapacity(averageEnergySquared, averageEnergy, temperature):
    """function to calculate heat capacity
        (<EE> - <E><E> ) / (kTT)
    """
    k = 1
    return (averageEnergySquared - (averageEnergy ** 2)) / (k * (temperature ** 2))
    

def calculateMagneticSusceptibilty(averageMagnetismSquared, averageMagnetism, temperature):       
    """function to calculate magnetic susceptibility
        (<MM> - <M><M> ) / (kT)
    """
    k = 1                                        
    return (averageMagnetismSquared - (averageMagnetism ** 2)) / (k * temperature)


def printValues(temp, J, mu, latticeLength):
    """Calculate and print values to output
    """ 
    valuesDict = calculateValues(temp, J, mu, latticeLength)
    print("averageEnergy: {}".format(valuesDict["averageEnergy"]))
    print("averageMagnetism: {}".format(valuesDict["averageMagnetism"]))
    
    heatCap = calculateHeatCapacity(valuesDict["averageEnergySquared"], valuesDict["averageEnergy"], valuesDict["temperature"])
    print("heatCapacity: {}".format(heatCap))
    
    magSusc = calculateMagneticSusceptibilty(valuesDict["averageMagnetismSquared"], valuesDict["averageMagnetism"], valuesDict["temperature"])
    print("magSusc: {}".format(magSusc))
    print("partition: {}".format(valuesDict["partition"]))


def plotValues(maxTemp, J, mu, latticeLength):
    """Calculate and plot values
        
        :param maxTemp: maximum tempurate that energy will be plotted to
        :param J: a constant that determines the energy scale
        :param mu: a constant that represents the magnetic moment of the system
        :param latticeLength: number of sites in spinConfigurations
    """
    temperatureValues = []
    averageEnergyValues = []
    averageMagnetismValues = []
    heatCapacityValues = []
    magneticSusceptibilityValues = []
    for t in range(1,maxTemp * 10):
        currentTemp = t / 10
        temperatureValues.append(currentTemp)
    #     call calculateValues
        values = calculateValues(currentTemp, J, mu, latticeLength)
    #     add averageEnergy and averageMagnetism values to lists
        averageEnergyValues.append(values["averageEnergy"])
        
        averageMagnetismValues.append(values["averageMagnetism"])
        
    #     add heatCapacity value to list
        heatCapacityValues.append(calculateHeatCapacity(values["averageEnergySquared"], values["averageEnergy"], values["temperature"]))
    # add magnetic susceptibility value to list
        magneticSusceptibilityValues.append(calculateMagneticSusceptibilty(values["averageMagnetismSquared"], values["averageMagnetism"], values["temperature"]))

    # plot average energy value"s
    plt.plot(temperatureValues, averageEnergyValues, label="<E>")
    plt.plot(temperatureValues, averageMagnetismValues, label="<M>")
    plt.plot(temperatureValues, heatCapacityValues, label="Heat Capacity")
    plt.plot(temperatureValues, magneticSusceptibilityValues, label="Magnetic Susceptibility")
    plt.legend()
    plt.show()

