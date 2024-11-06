import numpy as np
import unittest

def generate_random_data(importance: int, mean: int, variance: int, num_samples: int) -> dict:
    # generate random data using numpy
    user_threats = np.random.randint(max(mean - variance, 0),
                                          min(mean + variance + 1, 90), num_samples)
    department = {
        "importance" : importance,
        "user_threats" : user_threats
    }

    return department

def get_department_score(user_threats):
    #  Calculate the average threat score for a department.

    return np.mean(user_threats)

def get_aggregated_threat_score(departments: dict) -> int:
    """
        calculating aggregated score

        Calculate a weighted threat score for the entire company, considering both
        department importance and user count, while ensuring the score stays within 0-90.
    """

    total_weighted_score = 0
    total_weight = 0

    for department in departments:
        importance = departments["importance"]
        number_of_users = len(department["user_threats"])

        # Calculate the department's mean threat score
        mean = get_department_score(department["user_threats"])

        # Weight by both importance and user count
        weighted_score = mean * importance * number_of_users

        total_weighted_score += weighted_score

        # Accumulate the total weight as importance * number of users
        total_weight += importance * number_of_users

    # Calculate the final score and clip it to a maximum of 90
    aggregated_score = total_weighted_score / total_weight if total_weight != 0 else 0
    return min(aggregated_score, 90)

class TestSecurityCheck(unittest.TestCase):

    def test_department_score(self):
        # Check if the department score calculation works correctly
        scores = np.array([10, 20, 30])
        self.assertAlmostEqual(get_department_score(scores), 20, places=1)

    def test_aggregated_threat_score_uniform(self):
        # Test case with uniform threat scores across departments
        departments = [
            generate_random_data(50, 30, 5, 3),
            generate_random_data(50, 30, 5, 3),
            generate_random_data(50, 30, 5, 3),
            generate_random_data(50, 30, 5, 3),
            generate_random_data(50, 30, 5, 3)
        ]
        score = get_aggregated_threat_score(departments)
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 90)

    def test_aggregated_threat_score_high_variability(self):
        # High variability in threat scores and importance
        departments = [
            generate_random_data(100, 10, 5, 1),
            generate_random_data(200, 50, 10, 2),
            generate_random_data(150, 70, 20, 5),
            generate_random_data(100, 20, 10, 4),
            generate_random_data(50, 40, 5, 3)
        ]
        score = get_aggregated_threat_score(departments)
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 90)

    def test_aggregated_threat_score_single_high_threat(self):
        # Single department has high threat score
        departments = [
            generate_random_data(100, 5, 2, 1),
            generate_random_data(100, 5, 2, 1),
            generate_random_data(100, 90, 5, 5),  # High threat and high importance
            generate_random_data(100, 5, 2, 1),
            generate_random_data(100, 5, 2, 1)
        ]
        score = get_aggregated_threat_score(departments)
        self.assertGreater(score, 50)  # High importance should affect the score
        self.assertLessEqual(score, 90)

    def test_aggregated_threat_score_varying_user_counts(self):
        # Departments have varying user counts
        departments = [
            generate_random_data(10, 30, 5, 3),
            generate_random_data(200, 30, 5, 3),
            generate_random_data(100, 30, 5, 3),
            generate_random_data(50, 30, 5, 3),
            generate_random_data(150, 30, 5, 3)
        ]
        score = get_aggregated_threat_score(departments)
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 90)

    def test_aggregated_threat_score_outliers(self):
        # Departments contain outliers in threat scores
        departments = [
            generate_random_data(50, 30, 20, 3),
            generate_random_data(50, 10, 20, 2),
            generate_random_data(50, 60, 20, 5),
            generate_random_data(50, 45, 20, 4),
            generate_random_data(50, 20, 20, 1)
        ]
        score = get_aggregated_threat_score(departments)
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 90)




