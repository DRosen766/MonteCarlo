
import sys

import pytest

from MonteCarlo.SingleDimensionHamiltonian import SingleDimensionHamiltionian
from MonteCarlo.SpinConfiguration import spinConfiguration


def testSingleDimensionHamiltonian():
    assert(SingleDimensionHamiltionian(-2, 1.1, spinConfiguration(5, 4)).Hamiltonian == -8)
    assert(SingleDimensionHamiltionian(-2, 1.1, spinConfiguration(0, 2)).Hamiltonian == 4.0)

def testCalculateEnergy():
     assert(SingleDimensionHamiltionian(-2, 1.1, spinConfiguration(0, 2)).calculateEnergy() == 1.7999999999999998)
     assert(SingleDimensionHamiltionian(-2, 1.1, spinConfiguration(4, 7)).calculateEnergy() == 0.5)