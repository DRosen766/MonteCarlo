"""Provide the primary functions."""


# import classes
from .SpinConfiguration import *
from .SingleDimensionHamiltonian import *
import math


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


# for now only produces the configurations with two elements, should change soon
def generateSpinConfigurations(n):
    #generate spin configurations 
    spinConfigurations = []#convert each List in spinConfigurationsLists in SpinConfiguration object
    for binaryConfiguration in range(2 ** n):
        spinConfigurations.append(spinConfiguration(binaryConfiguration, n))

    return spinConfigurations


# calculates averageEnergy, averageMagnetism, HeatCapacity, and Magnetic Susceptibility
def calculateValues(temperature, J, mu, latticeLength):
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



# function to calculate heat capacity
def calculateHeatCapacity(averageEnergySquared, averageEnergy, temperature):
    k = 1
    #      (<EE> - <E><E> ) / (kTT)
    return (averageEnergySquared - (averageEnergy ** 2)) / (k * (temperature ** 2))
    

# function to calculate magnetic susceptibility
def calculateMagneticSusceptibilty(averageMagnetismSquared, averageMagnetism, temperature):       
    k = 1                                        
    # (<MM> - <M><M> ) / (kT)
    return (averageMagnetismSquared - (averageMagnetism ** 2)) / (k * temperature)


def printValues(temp, J, mu):
    valuesDict = calculateValues(temp, J, mu)
    print("averageEnergy: {}".format(valuesDict["averageEnergy"]))
    print("averageMagnetism: {}".format(valuesDict["averageMagnetism"]))
    
    heatCap = calculateHeatCapacity(valuesDict["averageEnergySquared"], valuesDict["averageEnergy"], valuesDict["temperature"])
    print("heatCapacity: {}".format(heatCap))
    
    magSusc = calculateMagneticSusceptibilty(valuesDict["averageMagnetismSquared"], valuesDict["averageMagnetism"], valuesDict["temperature"])
    print("magSusc: {}".format(magSusc))
    print("partition: {}".format(valuesDict["partition"]))


if __name__ == "__main__":
    print("HELLO WORLD")
    temperatureValues = []
    averageEnergyValues = []
    averageMagnetismValues = []
    heatCapacityValues = []
    magneticSusceptibilityValues = []
    for t in range(1,100):
        currentTemp = t / 10
        temperatureValues.append(currentTemp)
    #     call calculateValues
        values = calculateValues(currentTemp, -2, 1.1, 8)
    #     add averageEnergy and averageMagnetism values to lists
        averageEnergyValues.append(values["averageEnergy"])
        
        averageMagnetismValues.append(values["averageMagnetism"])
        
    #     add heatCapacity value to list
        heatCapacityValues.append(calculateHeatCapacity(values["averageEnergySquared"], values["averageEnergy"], values["temperature"]))
    # add magnetic susceptibility value to list
        magneticSusceptibilityValues.append(calculateMagneticSusceptibilty(values["averageMagnetismSquared"], values["averageMagnetism"], values["temperature"]))