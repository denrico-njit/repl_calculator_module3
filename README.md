# REPL Calculator

A simple command-line calculator with a Read-Eval-Print Loop (REPL) interface, built with Python.

## Setup

1. Clone the repository:
```bash
git clone git@github.com:denrico-njit/repl_calculator_module3.git
cd repl_calculator_module3
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux:
source venv/bin/activate

# Activate on Windows:
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the calculator:
```bash
python main.py
```

### Example Session
```
Still the World's Most Mediocre REPL Calculator

Enter an operation (add/subtract/multiply/divide) and two numbers, separated by spaces.
e.g. add 1 2
or type 'quit' to quit
Expression: add 5 3
Result: 8.0

Expression: multiply 4 2.5
Result: 10.0

Expression: divide 10 2
Result: 5.0

Expression: quit
Quitting
```

### Input Format

All inputs should follow the format: `<operation> <number1> <number2>`

**Supported operations:**
- `add` - Addition
- `subtract` - Subtraction
- `multiply` - Multiplication
- `divide` - Division

**Examples:**
- `add 5 3`
- `subtract 10 4`
- `multiply 3 4`
- `divide 10 2`

Numbers can be integers or decimals (e.g., 5, -3, 2.5, -1.75).

## Testing

Run tests:
```bash
python -m pytest --cov=app --cov-report=term-missing --cov-fail-under=100
```