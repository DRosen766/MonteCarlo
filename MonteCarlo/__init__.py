"""Package for Ising Hamiltonian"""
# import python packages
import math
import matplotlib.pyplot as plt

# Add imports here
from .Ising import *
from .SpinConfiguration import *
from .SingleDimensionHamiltonian import *
from .MonteCarloSampling import *
# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
