from src.utils import formation_data


def test_formation_data():
    assert formation_data("2019-06-16T22:17:01.825020") == "16.06.2019"