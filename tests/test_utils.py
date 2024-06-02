from src.utils import formation_data, formation_card


def test_formation_data():
    assert formation_data("2019-06-16T22:17:01.825020") == "16.06.2019"


def test_formation_card():
    assert formation_card("Maestro 1596837868705199") == "1596 83** **** 5199"