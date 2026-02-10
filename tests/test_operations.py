import pytest
from app.operations import addition, subtraction, multiplication, division


class TestAddition:
    """Test cases for addition function"""
    
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (0, 5, 5),
        (1.5, 2.5, 4.0),
        (0, 0, 0),
        (-1.5, 1.5, 0),
        (100, 200, 300),
    ])
    def test_addition_parametrized(self, a, b, expected):
        assert addition(a, b) == expected


class TestSubtraction:
    """Test cases for subtraction function"""
    
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),
        (3, 5, -2),
        (-2, -3, 1),
        (-2, 3, -5),
        (0, 5, -5),
        (5, 0, 5),
        (1.5, 0.5, 1.0),
        (0, 0, 0),
    ])
    def test_subtraction_parametrized(self, a, b, expected):
        assert subtraction(a, b) == expected


class TestMultiplication:
    """Test cases for multiplication function"""
    
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (-2, 3, -6),
        (-2, -3, 6),
        (0, 5, 0),
        (5, 0, 0),
        (1.5, 2, 3.0),
        (2.5, 4, 10.0),
        (-1, -1, 1),
    ])
    def test_multiplication_parametrized(self, a, b, expected):
        assert multiplication(a, b) == expected


class TestDivision:
    """Test cases for division function"""
    
    @pytest.mark.parametrize("a, b, expected", [
        (6, 2, 3),
        (5, 2, 2.5),
        (-6, 2, -3),
        (6, -2, -3),
        (-6, -2, 3),
        (0, 5, 0),
        (7, 2, 3.5),
    ])
    def test_division_parametrized(self, a, b, expected):
        assert division(a, b) == expected
    
    # Edge cases
    def test_division_by_zero(self):
        """Test that division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Division by zero is undefined"):
            division(5, 0)
    
    def test_division_by_zero_with_zero_numerator(self):
        """Test that 0/0 also raises ValueError"""
        with pytest.raises(ValueError, match="Division by zero is undefined"):
            division(0, 0)