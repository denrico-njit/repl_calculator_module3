import pytest
from app.calculator import calculator

# Note - opting for capsys instead of manual StringIO
# For reference: https://docs.pytest.org/en/6.2.x/capture.html
# Also: https://docs.pytest.org/en/6.2.x/reference.html?highlight=capsys#std-fixture-capsys
# Adapted from Prof. Williams' code at https://github.com/kaw393939/module2_is601/blob/main/tests/test_calculator.py

def run_calculator_with_input(monkeypatch, capsys, inputs):
    """
    Helper function to run calculator with simulated inputs and capture output.
    
    :param monkeypatch: pytest fixture to simulate user input
    :param capsys: pytest fixture to capture stdout
    :param inputs: list of string inputs to simulate
    :return: captured output as a string
    """
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    calculator()
    return capsys.readouterr().out


def test_calculator_addition(monkeypatch, capsys):
    """Test calculator with addition operation"""
    output = run_calculator_with_input(monkeypatch, capsys, ['add 5 3', 'quit'])
    assert 'Result: 8.0' in output


def test_calculator_subtraction(monkeypatch, capsys):
    """Test calculator with subtraction operation"""
    output = run_calculator_with_input(monkeypatch, capsys, ['subtract 10 4', 'quit'])
    assert 'Result: 6.0' in output


def test_calculator_multiplication(monkeypatch, capsys):
    """Test calculator with multiplication operation"""
    output = run_calculator_with_input(monkeypatch, capsys, ['multiply 3 4', 'quit'])
    assert 'Result: 12.0' in output


def test_calculator_division(monkeypatch, capsys):
    """Test calculator with division operation"""
    output = run_calculator_with_input(monkeypatch, capsys, ['divide 10 2', 'quit'])
    assert 'Result: 5.0' in output


def test_calculator_division_by_zero(monkeypatch, capsys):
    """Test calculator handles division by zero gracefully"""
    output = run_calculator_with_input(monkeypatch, capsys, ['divide 5 0', 'quit'])
    assert 'Division by zero is undefined' in output


def test_calculator_invalid_operation(monkeypatch, capsys):
    """Test calculator with invalid operation name"""
    output = run_calculator_with_input(monkeypatch, capsys, ['power 2 3', 'quit'])
    assert 'Invalid input' in output


def test_calculator_invalid_number_format(monkeypatch, capsys):
    """Test calculator with non-numeric input"""
    output = run_calculator_with_input(monkeypatch, capsys, ['add five three', 'quit'])
    assert 'Invalid input' in output


def test_calculator_multiple_operations(monkeypatch, capsys):
    """Test calculator with multiple operations in sequence"""
    output = run_calculator_with_input(monkeypatch, capsys, 
                                       ['add 2 3', 'multiply 4 5', 'subtract 10 3', 'quit'])
    assert 'Result: 5.0' in output
    assert 'Result: 20.0' in output
    assert 'Result: 7.0' in output