import yaml
import with_yaml_v1
import with_yaml_v2
import with_yaml_v3

def test_correct_number_of_days():
    with open('./sets.yaml') as f:
        sets = yaml.safe_load(f)['sets']
    expected = {'set1': 3, 'set2': 8, 'set3': 7, 'set4': 3}
    for k, v in expected.items():
        assert len(with_yaml_v1.calculate(False, sets[k])) == v, "incorrect number of days"
        assert len(with_yaml_v2.calculate(False, sets[k])) == v, "incorrect number of days"

def test_correct_number_of_days_with_datetime():
    with open('./sets_with_time.yaml') as f:
        sets = yaml.safe_load(f)['sets']
    expected = {'set1': 3, 'set2': 8, 'set3': 7, 'set4': 3, 'set5': 45, 'set6': 46}
    for k, v in expected.items():
        assert len(with_yaml_v3.calculate(False, sets[k])) == v, "incorrect number of days"
