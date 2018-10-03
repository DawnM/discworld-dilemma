import unittest
import app
# from string import ascii_uppercase


class TestQuiz(unittest.TestCase):
    """
    Our test suite for the Discworld Dilemma Quiz
    """
    
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)
    
