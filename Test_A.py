import pytest
import json
import numpy as np
from grades import gradeInfo

with open('keys.json', 'r') as json_file:
    expected_results = json.load(json_file)
random_files = random.sample(list(expected_results.keys()), 1)

def load_csv_data(csv_filepath):
    return pd.read_csv(csv_filepath)

@pytest.mark.parametrize("random_file", random_files)
def test_ansA(random_file):
    expected_count_trips = expected_results[random_file]["a"]
    csv_file = random_file.replace('.json', '.csv')
    actual_data = pd.read_csv(csv_file)
    actual_A = gradeInfo(actual_data, 2, 0.3)
    assert actual_count_trips == actual_A

