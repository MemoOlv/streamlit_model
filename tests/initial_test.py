from model import nothing


def tests_nothing():
    obtained = nothing()
    expected = "nothing"
    assert obtained == expected
