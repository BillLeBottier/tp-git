
from calculator import Calculator




def test_calculator():
    calcul=Calculator()
    assert calcul.addition(1,2)==3
    assert calcul.substraction(3, 2) == 1
    assert calcul.division(2,2) == 1

