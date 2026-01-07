# test_signalgenerator.py
"""
Tests for SignalGenerator module.
"""

import unittest
from signalgenerator import SignalGenerator

class TestSignalGenerator(unittest.TestCase):
    """Test cases for SignalGenerator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SignalGenerator()
        self.assertIsInstance(instance, SignalGenerator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SignalGenerator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
