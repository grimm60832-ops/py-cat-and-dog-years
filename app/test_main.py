from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_third_human_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_old_animal_age_to_human_year() -> None:
    assert get_human_age(100, 100) == [21, 17]
