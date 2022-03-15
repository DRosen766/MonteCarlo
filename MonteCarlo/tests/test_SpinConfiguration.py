# Import package, test suite, and other packages as needed
import sys
from bitarray import test

import pytest

from MonteCarlo.SpinConfiguration import *


def testSpinConfiguration():
    assert(spinConfiguration(0, 2).spins == [-1, -1])    
    assert(spinConfiguration(2, 2).spins == [1, -1])
    assert(spinConfiguration(1, 4).spins == [-1, -1, -1, 1])
    assert(spinConfiguration(15, 4).spins == [1, 1, 1, 1])

def testGetSpins():
    assert(spinConfiguration(0, 2).getNumElements() == 2)
    assert(spinConfiguration(0, 3).getNumElements() == 3)

def testCalculateMagnetism():
    assert(spinConfiguration(0, 2).calculateMagnetism() == -2)    
    assert(spinConfiguration(2, 2).calculateMagnetism() == 0)
    assert(spinConfiguration(1, 4).calculateMagnetism() == -2)
    assert(spinConfiguration(15, 4).calculateMagnetism() == 4)  