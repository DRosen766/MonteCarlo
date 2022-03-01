"""
Unit and regression test for the MonteCarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import MonteCarlo


def test_MonteCarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    print("working")
    assert "MonteCarlo" in sys.modules
