def test_hw():
    assert ('home', 'work') == ('home', 'work')


def test_qaqc():
    assert not "QA" == "QC"


def test_numbers():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
