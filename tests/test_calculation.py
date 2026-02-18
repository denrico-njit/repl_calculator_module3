import pytest
from app.calculation import (
    Calculation, 
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    PowerCalculation
)


class TestCalculationFactory:
    """Test cases for CalculationFactory"""
    
    def test_create_add_calculation(self):
        """Test factory creates AddCalculation correctly"""
        calc = CalculationFactory.create_calculation('add', 5, 3)
        assert isinstance(calc, AddCalculation)
        assert calc.a == 5
        assert calc.b == 3
        assert calc.execute() == 8
    
    def test_create_subtract_calculation(self):
        """Test factory creates SubtractCalculation correctly"""
        calc = CalculationFactory.create_calculation('subtract', 10, 4)
        assert isinstance(calc, SubtractCalculation)
        assert calc.execute() == 6
    
    def test_create_multiply_calculation(self):
        """Test factory creates MultiplyCalculation correctly"""
        calc = CalculationFactory.create_calculation('multiply', 3, 4)
        assert isinstance(calc, MultiplyCalculation)
        assert calc.execute() == 12
    
    def test_create_divide_calculation(self):
        """Test factory creates DivideCalculation correctly"""
        calc = CalculationFactory.create_calculation('divide', 10, 2)
        assert isinstance(calc, DivideCalculation)
        assert calc.execute() == 5
    
    def test_create_power_calculation(self):
        """Test factory creates PowerCalculation correctly"""
        calc = CalculationFactory.create_calculation('power', 2, 3)
        assert isinstance(calc, PowerCalculation)
        assert calc.execute() == 8
    
    def test_factory_case_insensitive(self):
        """Test that factory handles case-insensitive operation names"""
        calc_upper = CalculationFactory.create_calculation('ADD', 5, 3)
        calc_mixed = CalculationFactory.create_calculation('AdD', 5, 3)
        calc_lower = CalculationFactory.create_calculation('add', 5, 3)
        
        assert calc_upper.execute() == 8
        assert calc_mixed.execute() == 8
        assert calc_lower.execute() == 8
    
    def test_factory_invalid_operation(self):
        """Test that factory raises ValueError for unsupported operation"""
        with pytest.raises(ValueError, match="Unsupported calculation type"):
            CalculationFactory.create_calculation('invalid_op', 5, 3)
        
        with pytest.raises(ValueError, match="Available types"):
            CalculationFactory.create_calculation('ham_sandwich', 1, 2)
    
    def test_factory_duplicate_registration(self):
        """Test that registering duplicate calculation type raises error"""
        # This should raise ValueError because 'add' is already registered
        with pytest.raises(ValueError, match="already registered"):
            @CalculationFactory.register_calculation('add')
            class DuplicateAdd(Calculation):
                def execute(self):
                    return 0


class TestAddCalculation:
    """Test cases for AddCalculation"""
    
    def test_add_positive_numbers(self):
        calc = AddCalculation(5, 3)
        assert calc.execute() == 8
    
    def test_add_negative_numbers(self):
        calc = AddCalculation(-5, -3)
        assert calc.execute() == -8
    
    def test_add_mixed_signs(self):
        calc = AddCalculation(-5, 3)
        assert calc.execute() == -2
    
    def test_add_with_zero(self):
        calc = AddCalculation(5, 0)
        assert calc.execute() == 5
    
    def test_add_decimals(self):
        calc = AddCalculation(2.5, 3.7)
        assert calc.execute() == pytest.approx(6.2)
    
    def test_add_str_representation(self):
        calc = AddCalculation(5, 3)
        assert str(calc) == "AddCalculation: 5 Add 3 = 8"
    
    def test_add_repr(self):
        calc = AddCalculation(5, 3)
        assert repr(calc) == "AddCalculation(a=5, b=3)"


class TestSubtractCalculation:
    """Test cases for SubtractCalculation"""
    
    def test_subtract_positive_numbers(self):
        calc = SubtractCalculation(10, 4)
        assert calc.execute() == 6
    
    def test_subtract_negative_numbers(self):
        calc = SubtractCalculation(-10, -4)
        assert calc.execute() == -6
    
    def test_subtract_result_negative(self):
        calc = SubtractCalculation(3, 5)
        assert calc.execute() == -2
    
    def test_subtract_decimals(self):
        calc = SubtractCalculation(5.5, 2.3)
        assert calc.execute() == pytest.approx(3.2)
    
    def test_subtract_str_representation(self):
        calc = SubtractCalculation(10, 4)
        assert str(calc) == "SubtractCalculation: 10 Subtract 4 = 6"
    
    def test_subtract_repr(self):
        calc = SubtractCalculation(10, 4)
        assert repr(calc) == "SubtractCalculation(a=10, b=4)"


class TestMultiplyCalculation:
    """Test cases for MultiplyCalculation"""
    
    def test_multiply_positive_numbers(self):
        calc = MultiplyCalculation(3, 4)
        assert calc.execute() == 12
    
    def test_multiply_negative_numbers(self):
        calc = MultiplyCalculation(-3, -4)
        assert calc.execute() == 12
    
    def test_multiply_mixed_signs(self):
        calc = MultiplyCalculation(-3, 4)
        assert calc.execute() == -12
    
    def test_multiply_by_zero(self):
        calc = MultiplyCalculation(5, 0)
        assert calc.execute() == 0
    
    def test_multiply_decimals(self):
        calc = MultiplyCalculation(2.5, 4)
        assert calc.execute() == 10.0
    
    def test_multiply_str_representation(self):
        calc = MultiplyCalculation(3, 4)
        assert str(calc) == "MultiplyCalculation: 3 Multiply 4 = 12"
    
    def test_multiply_repr(self):
        calc = MultiplyCalculation(3, 4)
        assert repr(calc) == "MultiplyCalculation(a=3, b=4)"


class TestDivideCalculation:
    """Test cases for DivideCalculation"""
    
    def test_divide_positive_numbers(self):
        calc = DivideCalculation(10, 2)
        assert calc.execute() == 5
    
    def test_divide_negative_numbers(self):
        calc = DivideCalculation(-10, -2)
        assert calc.execute() == 5
    
    def test_divide_mixed_signs(self):
        calc = DivideCalculation(-10, 2)
        assert calc.execute() == -5
    
    def test_divide_decimals(self):
        calc = DivideCalculation(7, 2)
        assert calc.execute() == 3.5
    
    def test_divide_by_zero_raises_error(self):
        calc = DivideCalculation(10, 0)
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calc.execute()
    
    def test_divide_zero_by_zero_raises_error(self):
        calc = DivideCalculation(0, 0)
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calc.execute()
    
    def test_divide_str_representation(self):
        calc = DivideCalculation(10, 2)
        assert str(calc) == "DivideCalculation: 10 Divide 2 = 5.0"
    
    def test_divide_repr(self):
        calc = DivideCalculation(10, 2)
        assert repr(calc) == "DivideCalculation(a=10, b=2)"


class TestPowerCalculation:
    """Test cases for PowerCalculation"""
    
    def test_power_positive_numbers(self):
        calc = PowerCalculation(2, 3)
        assert calc.execute() == 8
    
    def test_power_to_zero(self):
        calc = PowerCalculation(5, 0)
        assert calc.execute() == 1
    
    def test_power_zero_to_positive(self):
        calc = PowerCalculation(0, 5)
        assert calc.execute() == 0
    
    def test_power_negative_base(self):
        calc = PowerCalculation(-2, 3)
        assert calc.execute() == -8
    
    def test_power_fractional_exponent(self):
        calc = PowerCalculation(49, 0.5)
        assert calc.execute() == pytest.approx(7.0)
    
    def test_power_negative_exponent(self):
        calc = PowerCalculation(2, -2)
        assert calc.execute() == pytest.approx(0.25)
    
    def test_power_str_representation(self):
        calc = PowerCalculation(2, 3)
        assert str(calc) == "PowerCalculation: 2 Power 3 = 8"
    
    def test_power_repr(self):
        calc = PowerCalculation(2, 3)
        assert repr(calc) == "PowerCalculation(a=2, b=3)"


class TestPolymorphism:
    """Test that different calculation types can be used interchangeably"""
    
    def test_calculations_through_common_interface(self):
        """Test that all calculations can be used polymorphically"""
        calculations = [
            AddCalculation(5, 3),
            SubtractCalculation(10, 4),
            MultiplyCalculation(3, 4),
            DivideCalculation(20, 4),
            PowerCalculation(2, 3)
        ]
        
        expected_results = [8, 6, 12, 5, 8]
        
        for calc, expected in zip(calculations, expected_results):
            assert calc.execute() == expected
    
    def test_calculations_in_list(self):
        """Test that calculations can be stored and executed from a list"""
        history = []
        
        history.append(CalculationFactory.create_calculation('add', 1, 2))
        history.append(CalculationFactory.create_calculation('multiply', 3, 4))
        history.append(CalculationFactory.create_calculation('subtract', 10, 3))
        
        results = [calc.execute() for calc in history]
        assert results == [3, 12, 7]


class TestAbstractCalculation:
    """Test that Calculation ABC cannot be instantiated directly"""
    
    def test_cannot_instantiate_abstract_class(self):
        """Test that attempting to instantiate Calculation raises TypeError"""
        with pytest.raises(TypeError):
            Calculation(5, 3)
