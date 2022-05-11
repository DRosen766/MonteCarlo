Getting Started
===============

.. raw:: html
        <h2>Installation and Usage</h2>
        <p><b>Before Installation: </b> Ensure numpy and matplotlib packages are installed</p>

        <p> To do a development install, download this repository and type <b>pip install -e .</b>in the root directory.</p>
        <P>
            <b>python MonteCarlo\Ising.py</b> from root directory to run Ising Hamiltonian calculations and plot results
        </P>
        <p>            
            <b>python MonteCarlo\MonteCarloSampling.py</b> from root directory to run MonteCarlo Sweep on Hamiltonian and plot results agains actual values
        </p>

        <h2>Modules and Examples</h2>
        <p>The examples in this section provides an overview of how to use each module and class.  The details of how all values are calculated in the class overview</p>
        <h3><a href="file:///C:/Users/Acemc/PHYS3684/MonteCarlo/docs/_build/html/api.html#module-MonteCarlo.Ising">Ising</a></h3>
        <p>
            This module includes a set of functions that are used to calculate and plot the average energy, average magnetism, heat capacity, and magnetic susceptibility for a one dimensional lattices of a given length.
            Do do this, all possible spin configurations with the appropriate length are calculated.  The above values are calculated at a given temperature and the process is repeated for all temperatures in some range.
        </p>
        
.. code-block:: python

    # import dependencies
    import numpy as np
    import matplotlib
    from matplotlib import pyplot as plt
    import math
    
    # import package and submodules
    import MonteCarlo
    from MonteCarlo import Ising
    from MonteCarlo import SpinConfiguration
    from MonteCarlo import SingleDimensionHamiltonian
    
    # assign the length of the spin configurations
    latticeLength = 5
    
    # create new list of spinConfiguration objects
    spinConfigList = MonteCarlo.Ising.generateSpinConfigurations(latticeLength)
    
    # print each spinConfigurations spins in binary
    print("spinCongfigurations: ")
    for sc in spinConfigList:
        print(sc.spins)
    
    # define temperature, J constant, mu constant, and lattice length
    temperature = 5
    J = -2
    mu = 1.1
    latticeLength = 4
    
    # calculate a dictionary of values
    values = MonteCarlo.Ising.calculateValues(temperature, J, mu, latticeLength)
    
    # call function do display the result of calling the above function
    # note: this will rerun the above function
    print("Values: ")
    MonteCarlo.Ising.printValues(temperature, J, mu, latticeLength)
    
    
    
    # call funtion to produce a plot of the results of the above function for temperatures between .1 and a maximum temp that you determine
    maxTemp = 10
    MonteCarlo.Ising.plotValues(maxTemp, J, mu, latticeLength)

.. raw:: html

        <h3><a href="file:///C:/Users/Acemc/PHYS3684/MonteCarlo/docs/_build/html/api.html#module-MonteCarlo.SpinConfiguration">Spin Configuration
        </a></h3>
        <p>
            This module contains the spinConfiguration class which includes functions for converting a bitstring into spins and calculating a spinConfiguration's magnetism.
        </p>

.. code-block:: python

    # import dependencies
    import numpy as np
    import matplotlib
    from matplotlib import pyplot as plt
    import math

    # import package and submodules
    import MonteCarlo
    from MonteCarlo import SpinConfiguration
    # import spinConfiguration class from SpinConfiguration Module
    from  MonteCarlo.SpinConfiguration import spinConfiguration

    # select the lattice length for this spinConfiguration\
    latticeLength = 5

    # select a decimal value that will be converted into a binary representation of the spins of this spinConfiguration
    # note this value must be between 0 and 2^latticeLength
    binaryConfiguration = 4


    spinConfig = spinConfiguration(binaryConfiguration, latticeLength)

    # display the converted binary representation of the integer that you entered
    print("Spins: {}".format(spinConfig.spins))


    # calculate and display the magnetism value of this spinConfiguration object
    print("Magnetism: {}".format(spinConfig.calculateMagnetism()))


.. raw:: html

        <h3><a href="file:///C:/Users/Acemc/PHYS3684/MonteCarlo/docs/_build/html/api.html#module-MonteCarlo.SingleDimensionHamiltonian">Single Dimension Hamiltonian</a></h3>
        <p>
            This module contains the SingleDimensionHamiltonian class which includes functions for building a hamiltonian from a given spin configuration and calculating its energy.
        </p>

.. code-block:: python

    # import dependencies
    import numpy as np
    import matplotlib
    from matplotlib import pyplot as plt
    import math

    # import package and submodules
    import MonteCarlo
    from MonteCarlo import SpinConfiguration
    from MonteCarlo import SingleDimensionHamiltonian

    # import SingleDimensionHamiltonian and spinConfiguration class
    from  MonteCarlo.SpinConfiguration import spinConfiguration
    from  MonteCarlo.SingleDimensionHamiltonian import SingleDimensionHamiltonian

    # create a spinConfiguration object
    spinConfig = spinConfiguration(10, 5)


    # define J and mu constants 
    J  = -2
    mu = 1.1

    # create a hamiltonian object
    ham = SingleDimensionHamiltonian(J, mu, spinConfig)

    # calculate and display the energy of this hamiltonian
    print("Energy: {}".format(ham.calculateEnergy()))

.. raw:: html
        <h3><a href= "file:///C:/Users/Acemc/PHYS3684/MonteCarlo/docs/_build/html/api.html#module-MonteCarlo.MonteCarloSampling">
            Single Dimension Hamiltonian</a></h3>
        <p>
            This module containts functions that perform a monte carlo sweep on a lattice to approximate its energy.
        </p>


Theory
------

This package uses the Ising mathematical model in order to calculate the energy of a Hamiltonian.




