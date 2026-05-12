# test_elasticcloud.py
"""
Tests for ElasticCloud module.
"""

import unittest
from elasticcloud import ElasticCloud

class TestElasticCloud(unittest.TestCase):
    """Test cases for ElasticCloud class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ElasticCloud()
        self.assertIsInstance(instance, ElasticCloud)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ElasticCloud()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
