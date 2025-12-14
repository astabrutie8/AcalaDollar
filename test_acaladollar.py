# test_acaladollar.py
"""
Tests for AcalaDollar module.
"""

import unittest
from acaladollar import AcalaDollar

class TestAcalaDollar(unittest.TestCase):
    """Test cases for AcalaDollar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AcalaDollar()
        self.assertIsInstance(instance, AcalaDollar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AcalaDollar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
