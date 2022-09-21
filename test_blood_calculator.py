# test_blood_calculator.py


# Testing Function 1: check_HDL, which evaluates HDL values into three different categories: Normal, Borderline Low and Low
#Approach 1
'''
def test_check_HDL_Normal():
    from blood_calculator import check_HDL #For readibility we will do imports of fxns to test within the testing function
    answer=check_HDL(85)
    expected="Normal"
    assert answer==expected
def test_check_HDL_BorderLow():
    from blood_calculator import check_HDL
    answer=check_HDL(55)
    expected="Borderline Low"
    assert answer==expected
def test_check_HDL_Low():
    from blood_calculator import check_HDL
    answer=check_HDL(35)
    expected="Low"
    assert answer==expected
'''
#Approach 2 --This is not best practice... It will tell that there is an error but doesn't finish the testing which will be worse in the long run
'''
def test_check_HDL():
    from blood_calculator import check_HDL #For readibility we will do imports of fxns to test within the testing function
    answer=check_HDL(85)
    expected="Normal"
    assert answer==expected
    answer=check_HDL(55)
    expected="Borderline Low"
    assert answer==expected
    answer=check_HDL(35)
    expected="Low"
    assert answer==expected
'''

#Approach 3: Assign different values with the pytest decorator (which is marked with the @ symbol). This will run all of the tests and tell which one has failed, while also running all trials. This is the best coding practice

import pytest

@pytest.mark.parametrize("HDL_value,expected",
[(85,"Normal"),
(55,"Borderline Low"),
(35,"Low")])

def test_check_HDL_Normal(HDL_value,expected):
    from blood_calculator import check_HDL #For readibility we will do imports of fxns to test within the testing function
    answer=check_HDL(HDL_value)
    assert answer==expected


@pytest.mark.parametrize("LDL_Value, expected",
[(120, "Normal"),
(145,"Borderline High"),
(180,"High"),
(200,"Very High")])

def test_check_LDL(LDL_Value, expected):
    from blood_calculator import check_LDL
    answer=check_LDL(LDL_Value)
    assert answer==expected


@pytest.mark.parametrize("Cholesterol, expected",
[(250, "High"),
(220, "Borderline High"),
(190, "Normal")])

def test_check_cholesterol(Cholesterol, expected):
    from blood_calculator import check_cholesterol
    answer=check_cholesterol(Cholesterol)
    assert answer==expected
#Add also cholesterol...
