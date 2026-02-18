import pytest
from app.calculator import calculator, display_help, display_history
from app.calculation import AddCalculation, MultiplyCalculation

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


# ============================================================================
# Basic Operation Tests
# ============================================================================

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


def test_calculator_power(monkeypatch, capsys):
    """Test calculator with exponentiation (power) operation"""
    output = run_calculator_with_input(monkeypatch, capsys, ['power 2 3', 'quit'])
    assert 'Result: 8.0' in output


# ============================================================================
# Error Handling Tests
# ============================================================================

def test_calculator_division_by_zero(monkeypatch, capsys):
    """Test calculator handles division by zero gracefully"""
    output = run_calculator_with_input(monkeypatch, capsys, ['divide 5 0', 'quit'])
    assert 'Cannot divide by zero' in output
    assert 'Please enter a non-zero divisor' in output


def test_calculator_invalid_operation(monkeypatch, capsys):
    """Test calculator with invalid operation name"""
    output = run_calculator_with_input(monkeypatch, capsys, ['ham_sandwich 2 3', 'quit'])
    assert 'Invalid input' in output
    assert 'Type \'help\' to see the list of valid operations' in output


def test_calculator_invalid_number_format(monkeypatch, capsys):
    """Test calculator with non-numeric input"""
    output = run_calculator_with_input(monkeypatch, capsys, ['add five three', 'quit'])
    assert 'Invalid input' in output
    assert 'Use the format <operation> <num1> <num2>' in output


def test_calculator_too_few_arguments(monkeypatch, capsys):
    """Test calculator with too few arguments"""
    output = run_calculator_with_input(monkeypatch, capsys, ['add 5', 'quit'])
    assert 'Invalid input' in output


def test_calculator_too_many_arguments(monkeypatch, capsys):
    """Test calculator with too many arguments"""
    output = run_calculator_with_input(monkeypatch, capsys, ['add 1 2 3', 'quit'])
    assert 'Invalid input' in output


def test_calculator_no_arguments(monkeypatch, capsys):
    """Test calculator with operation but no numbers"""
    output = run_calculator_with_input(monkeypatch, capsys, ['add', 'quit'])
    assert 'Invalid input' in output


def test_calculator_generic_exception_handling(monkeypatch, capsys):
    """Test that calculator handles unexpected exceptions gracefully"""
    # We'll use a mock that raises a generic exception when execute is called
    def mock_input_causing_exception(prompt):
        calls = mock_input_causing_exception.calls
        mock_input_causing_exception.calls += 1
        if calls == 0:
            return 'add 1 2'  # This will work initially
        elif calls == 1:
            return 'quit'
    
    mock_input_causing_exception.calls = 0
    
    # Patch to make execute() raise a generic exception
    from app.calculation import AddCalculation
    original_execute = AddCalculation.execute
    
    def failing_execute(self):
        raise RuntimeError("Unexpected error")
    
    monkeypatch.setattr('builtins.input', mock_input_causing_exception)
    monkeypatch.setattr(AddCalculation, 'execute', failing_execute)
    
    calculator()
    captured = capsys.readouterr()
    
    assert 'Something unforseen has happened' in captured.out
    assert 'Please try again' in captured.out
    
    # Restore original
    monkeypatch.setattr(AddCalculation, 'execute', original_execute)


# ============================================================================
# Special Command Tests
# ============================================================================

def test_calculator_help_command(monkeypatch, capsys):
    """Test that 'help' command displays help message"""
    output = run_calculator_with_input(monkeypatch, capsys, ['help', 'quit'])
    assert 'Calculator Help' in output
    assert 'Supported operations:' in output
    assert 'add' in output
    assert 'subtract' in output
    assert 'multiply' in output
    assert 'divide' in output
    assert 'power' in output


def test_calculator_history_empty(monkeypatch, capsys):
    """Test that history command shows message when empty"""
    output = run_calculator_with_input(monkeypatch, capsys, ['history', 'quit'])
    assert 'Nothing to see here yet' in output


def test_calculator_history_with_calculations(monkeypatch, capsys):
    """Test that history shows previous calculations"""
    output = run_calculator_with_input(monkeypatch, capsys, 
                                       ['add 5 3', 'multiply 4 2', 'history', 'quit'])
    assert 'Previous Calculations:' in output
    assert '1.' in output
    assert 'AddCalculation' in output
    assert '2.' in output
    assert 'MultiplyCalculation' in output


def test_calculator_exit_command(monkeypatch, capsys):
    """Test that 'exit' command quits the calculator"""
    output = run_calculator_with_input(monkeypatch, capsys, ['add 1 1', 'exit'])
    assert 'Quitting' in output


def test_calculator_quit_lowercase(monkeypatch, capsys):
    """Test that 'quit' command works (already tested but explicitly named)"""
    output = run_calculator_with_input(monkeypatch, capsys, ['quit'])
    assert 'Quitting' in output


def test_calculator_q_command(monkeypatch, capsys):
    """Test that 'q' command quits the calculator"""
    output = run_calculator_with_input(monkeypatch, capsys, ['q'])
    assert 'Quitting' in output


def test_calculator_quit_uppercase(monkeypatch, capsys):
    """Test that 'QUIT' command works (case insensitive)"""
    output = run_calculator_with_input(monkeypatch, capsys, ['QUIT'])
    assert 'Quitting' in output


def test_calculator_exit_uppercase(monkeypatch, capsys):
    """Test that 'EXIT' command works (case insensitive)"""
    output = run_calculator_with_input(monkeypatch, capsys, ['EXIT'])
    assert 'Quitting' in output


# ============================================================================
# Multiple Operations Tests
# ============================================================================

def test_calculator_multiple_operations(monkeypatch, capsys):
    """Test calculator with multiple operations in sequence"""
    output = run_calculator_with_input(monkeypatch, capsys, 
                                       ['add 2 3', 'multiply 4 5', 'subtract 10 3', 'quit'])
    assert 'Result: 5.0' in output
    assert 'Result: 20.0' in output
    assert 'Result: 7.0' in output
    assert 'Quitting' in output


def test_calculator_operations_with_errors_then_success(monkeypatch, capsys):
    """Test that calculator continues after errors"""
    output = run_calculator_with_input(monkeypatch, capsys,
                                       ['divide 5 0', 'invalid_op 1 2', 'add 3 4', 'quit'])
    assert 'Cannot divide by zero' in output
    assert 'Invalid input' in output
    assert 'Result: 7.0' in output


# ============================================================================
# Interrupt Handling Tests
# ============================================================================

def test_calculator_keyboard_interrupt(monkeypatch, capsys):
    """Test that KeyboardInterrupt (Ctrl+C) is handled gracefully"""
    def mock_input_with_interrupt(prompt):
        raise KeyboardInterrupt()
    
    monkeypatch.setattr('builtins.input', mock_input_with_interrupt)
    calculator()
    captured = capsys.readouterr()
    assert 'KeyboardInterrupt detected' in captured.out
    assert 'Exiting' in captured.out


def test_calculator_eof_error(monkeypatch, capsys):
    """Test that EOFError (Ctrl+D) is handled gracefully"""
    def mock_input_with_eof(prompt):
        raise EOFError()
    
    monkeypatch.setattr('builtins.input', mock_input_with_eof)
    calculator()
    captured = capsys.readouterr()
    assert 'EOF Detected' in captured.out
    assert 'Exiting' in captured.out


# ============================================================================
# Helper Function Tests (Direct Testing)
# ============================================================================

def test_display_help_function(capsys):
    """Test display_help function directly"""
    display_help()
    captured = capsys.readouterr()
    assert 'Calculator Help' in captured.out
    assert 'Usage:' in captured.out
    assert 'add' in captured.out
    assert 'subtract' in captured.out
    assert 'multiply' in captured.out
    assert 'divide' in captured.out
    assert 'power' in captured.out
    assert 'Examples:' in captured.out


def test_display_history_empty_directly(capsys):
    """Test display_history function with empty history"""
    display_history([])
    captured = capsys.readouterr()
    assert 'Nothing to see here yet' in captured.out


def test_display_history_with_items_directly(capsys):
    """Test display_history function with calculations"""
    history = [
        AddCalculation(5, 3),
        MultiplyCalculation(4, 2)
    ]
    display_history(history)
    captured = capsys.readouterr()
    assert 'Previous Calculations:' in captured.out
    assert '1.' in captured.out
    assert '2.' in captured.out
    assert 'AddCalculation' in captured.out
    assert 'MultiplyCalculation' in captured.out


# ============================================================================
# Edge Cases
# ============================================================================

def test_calculator_whitespace_only_input(monkeypatch, capsys):
    """Test that empty input (just whitespace) is handled"""
    # The empty string continuation has pragma: no cover
    # but we can still test it behaves correctly
    output = run_calculator_with_input(monkeypatch, capsys, ['   ', 'add 1 1', 'quit'])
    assert 'Result: 2.0' in output


def test_calculator_decimal_numbers(monkeypatch, capsys):
    """Test calculator with decimal numbers"""
    output = run_calculator_with_input(monkeypatch, capsys, ['add 1.5 2.3', 'quit'])
    assert 'Result: 3.8' in output


def test_calculator_negative_numbers(monkeypatch, capsys):
    """Test calculator with negative numbers"""
    output = run_calculator_with_input(monkeypatch, capsys, ['add -5 3', 'quit'])
    assert 'Result: -2.0' in output