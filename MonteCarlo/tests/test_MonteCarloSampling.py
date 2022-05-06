from MonteCarlo.MonteCarloSampling import MonteCarloSampling
from MonteCarlo.SpinConfiguration import spinConfiguration
from MonteCarlo.SingleDimensionHamiltonian import SingleDimensionHamiltonian

def testConstructor():
    mcSample = MonteCarloSampling(15, 15, 1, 1, 1)
    assert(mcSample.sites == 15)
    assert(mcSample.steps == 15)
    assert(mcSample.J == 1)
    assert(mcSample.mu == 1)
    assert(mcSample.temperature == 1)

# def testSweep():
