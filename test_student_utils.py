import unittest
import student_utilss as utils
class TestStudentUtils(unittest.TestCase):
    """Verify accuracy of score calculation utilities."""
    @classmethod
    def setUpClass(cls):
        """Define shared sample scores once for all test cases."""
        cls.sample_scores = [90, 80, 70]

    def test_average_calculation(self):
        """Check that average score matches expected float value."""
        actual = utils.calculate_average(self.sample_scores)
        self.assertAlmostEqual(actual, 80.0)

    def test_highest_value(self):
        """Check that highest score is identified accurately."""
        actual = utils.get_highest_score(self.sample_scores)
        self.assertEqual(actual, 90)

    def test_lowest_value(self):
        """Check that lowest score is identified accurately."""
        actual = utils.get_lowest_score(self.sample_scores)
        self.assertEqual(actual, 70)
if __name__ == "__main__":
    unittest.main()
