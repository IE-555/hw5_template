import pytest
import json
import numpy as np
import pandas as pd
import random
from grades import gradeInfo

with open('keys.json', 'r') as json_file:
    expected_results = json.load(json_file)
random_files = random.sample(list(expected_results.keys()), 1)


@pytest.mark.parametrize("random_file", random_files)
def test_ansA(random_file):
    expected = expected_results[random_file]["d"]
    csv_file = random_file.replace('.json', '.csv')
    actual_D = gradeInfo(csv_file, 2, 0.3)[3]
    assert expected == actual_D
