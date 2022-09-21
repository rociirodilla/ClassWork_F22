# test_blood_calculator.py
import pytest


@pytest.mark.parametrize("HDL_value, expected",
                         [(85, "Normal"),
                          (55, "Borderline Low"),
                          (35, "Low")])
def test_check_HDL_Normal(HDL_value, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_value)
    assert answer == expected


@pytest.mark.parametrize("LDL_Value, expected",
                         [(120, "Normal"),
                          (145, "Borderline High"),
                          (180, "High"),
                          (200, "Very High")])
def test_check_LDL(LDL_Value, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL_Value)
    assert answer == expected


@pytest.mark.parametrize("Cholesterol, expected",
                         [(250, "High"),
                          (220, "Borderline High"),
                          (190, "Normal")])
def test_check_cholesterol(Cholesterol, expected):
    from blood_calculator import check_cholesterol
    answer = check_cholesterol(Cholesterol)
    assert answer == expected
