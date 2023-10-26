from testfunction import isLeapYear

def test_shotyear():
    assert isLeapYear(2012) == True
    assert isLeapYear(2024) == True
    assert isLeapYear(2400) == True

def test_not_shotyear():
    assert isLeapYear(1300) == False
    assert isLeapYear(1400) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(2100) == False

def test_if_year_divides_four_and_not_onehundred():
    assert isLeapYear(2016) == True
    assert isLeapYear(2020) == True

def test_if_year_divides_onehundred_and_not_fourhundred():
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False

def test_if_year_not_divides_four():
    assert isLeapYear(2013) == False
    assert isLeapYear(2009) == False
