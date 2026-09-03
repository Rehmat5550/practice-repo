from calculator import Calculator

def test_add():
    # 1. Arrange
    calc = Calculator()
    
    # 2. Act
    result = calc.add(10, 5)
    
    # 3. Assert (Prove it works)
    assert result == 15
def test_divide():

    calc = Calculator()

    another_result = calc.divide(10, 2)
    assert another_result == 5.0

def test_multiply():
    calc = Calculator()
    f_results = calc.multiply(5, 5)
    assert f_results == 25

