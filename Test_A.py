import pytest
import json
import numpy as np
import grades  

with open('keys.json', 'r') as json_file:
    expected_results = json.load(json_file)
    print(expected_results['example_4']['a'])

@pytest.mark.parametrize("filename, numExams, hwWeight, expected_ansA", [
    ('grades_example_4.csv', 2, 0.3, expected_results['example_4']['a']),
    # Add more test cases if needed
])
def test_ansA(filename, numExams, hwWeight, expected_ansA):
    result = grades.gradeInfo(filename, numExams, hwWeight)
    assert result[0] == expected_ansA

