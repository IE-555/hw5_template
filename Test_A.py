import pytest
import json
import numpy as np
import pandas as pd
import random
import math
from grades import gradeInfo

with open('keys.json', 'r') as json_file:
    expected_results = json.load(json_file)
random_files = random.sample(list(expected_results.keys()), 1)


@pytest.mark.parametrize("random_file", random_files)
def test_ansA(random_file):
    expected = expected_results[random_file]["a"]
    csv_file = random_file.replace('.json', '.csv')
    actual_A = gradeInfo(csv_file, 2, 0.3)[0]
    assert math.isclose(expected, actual_A, rel_tol=1e-4, abs_tol=1e-4)


