import numpy as np
import unittest

def generate_random_data(department: str, mean: int, variance: int, num_samples: int) -> dict:
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
        self.assertAlmostEqual()
        pass
