# Simple Calculator MCP Server

A production-ready Model Context Protocol (MCP) server that provides comprehensive mathematical calculation tools for basic arithmetic, advanced operations, and expression evaluation. Supports both integer and floating-point numbers.

## Features

- **12 Mathematical Tools**:
  - Basic Arithmetic: `add`, `subtract`, `multiply`, `divide`
  - Advanced Operations: `power`, `square_root`, `modulo`
  - Utility Functions: `absolute`, `round`, `factorial`, `percentage`
  - Expression Evaluator: `evaluate_expression` (supports complex mathematical expressions)

- **Multiple Transport Modes**:
  - `sse` - Server-Sent Events for web clients (default)
  - `stdio` - Standard input/output for Claude Desktop, Cursor
  - `streamable-http` - MCP v1 preferred HTTP mode

- **Safe Expression Evaluation**: Supports standard math functions (sqrt, pow, sin, cos, log, etc.)
- **Production-Ready**: Comprehensive error handling, logging, and health endpoints

## Installation

```bash
cd simple-calculator-mcp
pip install -e .
```

## Usage

### SSE Mode (Default - for Web Clients)
```bash
calculator-mcp
# Or explicitly specify:
calculator-mcp --mode sse --port 8000
```

### stdio Mode (for Claude Desktop/Cursor)
```bash
calculator-mcp --mode stdio
```

### Streamable HTTP Mode (MCP v1)
```bash
calculator-mcp --mode streamable-http --port 8000
```

## Tools

> Numeric tool inputs now accept raw numbers or numeric strings (for example: `"4.2"`).
>
### Basic Arithmetic

#### add
Add two numbers together.

**Parameters:**
- `a` (number or numeric string): First number
- `b` (number or numeric string): Second number

**Example:** `a: 3.14, b: 2.0` → `5.14`

#### subtract
Subtract second number from first number.

**Parameters:**
- `a` (number or numeric string): First number
- `b` (number or numeric string): Second number

**Example:** `a: 10.5, b: 3.2` → `7.3`

#### multiply
Multiply two numbers together.

**Parameters:**
- `a` (number or numeric string): First number
- `b` (number or numeric string): Second number

**Example:** `a: 2.5, b: 4.0` → `10.0`

#### divide
Divide the first number by the second number.

**Parameters:**
- `dividend` (number or numeric string): The number to be divided
- `divisor` (number or numeric string): The number to divide by

**Example:** `dividend: 10.5, divisor: 2.0` → `5.25`

### Advanced Operations

#### power
Raise a base number to the power of an exponent.

**Parameters:**
- `base` (number or numeric string): The base number
- `exponent` (number or numeric string): The exponent (power)

**Example:** `base: 2.0, exponent: 3.0` → `8.0`

#### square_root
Calculate the square root of a number.

**Parameters:**
- `number` (number or numeric string): The number to find the square root of (must be ≥ 0)

**Example:** `16.0` → `4.0`

#### modulo
Calculate the remainder when dividing.

**Parameters:**
- `dividend` (number or numeric string): The number to be divided
- `divisor` (number or numeric string): The number to divide by

**Example:** `dividend: 17.5, divisor: 5.0` → `2.5`

### Utility Functions

#### absolute
Calculate the absolute value of a number.

**Parameters:**
- `number` (number or numeric string): The number to find the absolute value of

**Example:** `-42.5` → `42.5`

#### round
Round a number to specified decimal places.

**Parameters:**
- `number` (number or numeric string): The number to round
- `decimals` (integer or numeric string, optional): Number of decimal places (default: 0)

**Example:** `number: 3.14159, decimals: 2` → `3.14`

#### factorial
Calculate the factorial of a non-negative integer.

**Parameters:**
- `number` (integer or numeric string): The non-negative integer

**Example:** `5` → `120` (5! = 5×4×3×2×1)

#### percentage
Calculate percentage of a number or what percentage a value represents.

**Parameters:**
- `value` (number or numeric string): The value or percentage amount
- `total` (number or numeric string): The total value or base number
- `mode` (string, optional): 'of' or 'is' (default: 'of')
  - `of`: calculates value% of total (e.g., 20% of 100)
  - `is`: calculates what percentage value is of total (e.g., 20 is what % of 100)

**Examples:**
- `value: 20, total: 100, mode: "of"` → `20.0` (20% of 100)
- `value: 25, total: 100, mode: "is"` → `25.0` (25 is 25% of 100)

### Expression Evaluator

#### evaluate_expression
Evaluate a mathematical expression string.

**Parameters:**
- `expression` (string): Mathematical expression to evaluate

**Supported operations:** `+`, `-`, `*`, `/`, `**` (power), `()`

**Supported functions:** `sqrt`, `pow`, `abs`, `round`, `floor`, `ceil`, `sin`, `cos`, `tan`, `log`, `log10`, `exp`

**Constants:** `pi`, `e`

**Examples:**
- `"2 + 3 * 4"` → `14`
- `"sqrt(16) + pow(2, 3)"` → `12`
- `"sin(pi/2)"` → `1.0`

## Configuration

### For Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "calculator": {
      "command": "calculator-mcp"
    }
  }
}
```

### For SSE Mode

```json
{
  "mcpServers": {
    "calculator": {
      "url": "http://localhost:8000/sse"
    }
  }
}
```

## Health Checks

- `GET /` - Root endpoint (returns transport mode)
- `GET /health` - Health check endpoint

## Architecture

```
simple-calculator-mcp/
├── calculator_server.py       # Main server with transport modes
├── tools/
│   ├── __init__.py
│   ├── toolhandler.py         # Abstract base class
│   └── calculator_tools.py    # 12 calculator tool implementations
├── pyproject.toml             # Package configuration
├── LICENSE
└── README.md
```

## Requirements

- Python 3.10+
- mcp[cli] >= 1.12.0
- starlette >= 0.27.0
- uvicorn >= 0.20.0

## Error Handling

The server provides clear error messages for:
- Division by zero
- Square root of negative numbers
- Invalid expressions
- Missing required parameters
- Invalid parameter types

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions, please visit the repository.
