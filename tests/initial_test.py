import pandas as pd

from model import multiplier


def test_multiplier():
    data = {"time": [1, 2, 3], "value": [3, 2, 1]}
    df = pd.DataFrame(data)
    times = 2
    obtained = multiplier(df, times=times)
    obtained_values = obtained["value"].values
    expected_values = [6, 4, 2]
    assert (obtained_values == expected_values).all()
