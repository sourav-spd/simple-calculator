"""Calculator tool implementations for MCP server."""

import json
import math
from collections.abc import Sequence
from typing import Any

from mcp.types import TextContent, Tool

from .toolhandler import ToolHandler


class AddToolHandler(ToolHandler):
    """Add two numbers."""

    def __init__(self) -> None:
        super().__init__("add")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Add",
            description="Add two numbers and return the result.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "a": {"type": "number", "description": "First number."},
                    "b": {"type": "number", "description": "Second number."},
                },
                "required": ["a", "b"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["a", "b"])
        a = float(args["a"])
        b = float(args["b"])
        
        result = a + b
        
        response = {
            "operation": "addition",
            "a": a,
            "b": b,
            "result": result,
            "equation": f"{a} + {b} = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class SubtractToolHandler(ToolHandler):
    """Subtract two numbers."""

    def __init__(self) -> None:
        super().__init__("subtract")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Subtract",
            description="Subtract second number from first number.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "a": {"type": "number", "description": "First number."},
                    "b": {"type": "number", "description": "Second number."},
                },
                "required": ["a", "b"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["a", "b"])
        a = float(args["a"])
        b = float(args["b"])
        
        result = a - b
        
        response = {
            "operation": "subtraction",
            "a": a,
            "b": b,
            "result": result,
            "equation": f"{a} - {b} = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class MultiplyToolHandler(ToolHandler):
    """Multiply two numbers."""

    def __init__(self) -> None:
        super().__init__("multiply")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Multiply",
            description="Multiply two numbers and return the result.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "a": {"type": "number", "description": "First number."},
                    "b": {"type": "number", "description": "Second number."},
                },
                "required": ["a", "b"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["a", "b"])
        a = float(args["a"])
        b = float(args["b"])
        
        result = a * b
        
        response = {
            "operation": "multiplication",
            "a": a,
            "b": b,
            "result": result,
            "equation": f"{a} × {b} = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class DivideToolHandler(ToolHandler):
    """Divide two numbers."""

    def __init__(self) -> None:
        super().__init__("divide")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Divide",
            description="Divide the first number by the second number.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "dividend": {
                        "type": "number",
                        "description": "The number to be divided",
                    },
                    "divisor": {
                        "type": "number",
                        "description": "The number to divide by",
                    },
                },
                "required": ["dividend", "divisor"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["dividend", "divisor"])
        dividend = float(args["dividend"])
        divisor = float(args["divisor"])
        
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        
        result = dividend / divisor
        
        response = {
            "operation": "division",
            "dividend": dividend,
            "divisor": divisor,
            "result": result,
            "equation": f"{dividend} ÷ {divisor} = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class PowerToolHandler(ToolHandler):
    """Raise a number to a power."""

    def __init__(self) -> None:
        super().__init__("power")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Power",
            description="Raise a base number to the power of an exponent.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "base": {
                        "type": "number",
                        "description": "The base number",
                    },
                    "exponent": {
                        "type": "number",
                        "description": "The exponent (power)",
                    },
                },
                "required": ["base", "exponent"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["base", "exponent"])
        base = float(args["base"])
        exponent = float(args["exponent"])
        
        result = base ** exponent
        
        response = {
            "operation": "power",
            "base": base,
            "exponent": exponent,
            "result": result,
            "equation": f"{base}^{exponent} = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class SquareRootToolHandler(ToolHandler):
    """Calculate square root of a number."""

    def __init__(self) -> None:
        super().__init__("square_root")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Square Root",
            description="Calculate the square root of a number.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "number": {
                        "type": "number",
                        "description": "The number to find the square root of",
                        "minimum": 0,
                    }
                },
                "required": ["number"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["number"])
        number = float(args["number"])
        
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        
        result = math.sqrt(number)
        
        response = {
            "operation": "square_root",
            "number": number,
            "result": result,
            "equation": f"√{number} = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class ModuloToolHandler(ToolHandler):
    """Calculate modulo (remainder) of division."""

    def __init__(self) -> None:
        super().__init__("modulo")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Modulo",
            description="Calculate the remainder when dividing the first number by the second.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "dividend": {
                        "type": "number",
                        "description": "The number to be divided",
                    },
                    "divisor": {
                        "type": "number",
                        "description": "The number to divide by",
                    },
                },
                "required": ["dividend", "divisor"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["dividend", "divisor"])
        dividend = float(args["dividend"])
        divisor = float(args["divisor"])
        
        if divisor == 0:
            raise ValueError("Cannot calculate modulo with divisor of zero")
        
        result = dividend % divisor
        
        response = {
            "operation": "modulo",
            "dividend": dividend,
            "divisor": divisor,
            "result": result,
            "equation": f"{dividend} mod {divisor} = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class AbsoluteToolHandler(ToolHandler):
    """Calculate absolute value of a number."""

    def __init__(self) -> None:
        super().__init__("absolute")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Absolute Value",
            description="Calculate the absolute value of a number.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "number": {
                        "type": "number",
                        "description": "The number to find the absolute value of",
                    }
                },
                "required": ["number"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["number"])
        number = float(args["number"])
        
        result = abs(number)
        
        response = {
            "operation": "absolute_value",
            "number": number,
            "result": result,
            "equation": f"|{number}| = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class RoundToolHandler(ToolHandler):
    """Round a number to specified decimal places."""

    def __init__(self) -> None:
        super().__init__("round")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Round Number",
            description="Round a number to a specified number of decimal places.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "number": {
                        "type": "number",
                        "description": "The number to round",
                    },
                    "decimals": {
                        "type": "integer",
                        "description": "Number of decimal places to round to",
                        "default": 0,
                        "minimum": 0,
                    },
                },
                "required": ["number"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["number"])
        number = float(args["number"])
        decimals = args.get("decimals", 0)
        
        result = round(number, decimals)
        
        response = {
            "operation": "round",
            "number": number,
            "decimals": decimals,
            "result": result,
            "equation": f"round({number}, {decimals}) = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class FactorialToolHandler(ToolHandler):
    """Calculate factorial of a number."""

    def __init__(self) -> None:
        super().__init__("factorial")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Factorial",
            description="Calculate the factorial of a non-negative integer.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "number": {
                        "type": "integer",
                        "description": "The non-negative integer to calculate factorial of",
                        "minimum": 0,
                    }
                },
                "required": ["number"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["number"])
        number = args["number"]
        
        if number < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        
        result = math.factorial(number)
        
        response = {
            "operation": "factorial",
            "number": number,
            "result": result,
            "equation": f"{number}! = {result}",
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class PercentageToolHandler(ToolHandler):
    """Calculate percentage of a number."""

    def __init__(self) -> None:
        super().__init__("percentage")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Percentage",
            description="Calculate what percentage of a total a value represents, or calculate a percentage of a number.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The value or percentage amount",
                    },
                    "total": {
                        "type": "number",
                        "description": "The total value or base number",
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["of", "is"],
                        "description": "'of' calculates percentage of a number (e.g., 20% of 100), 'is' calculates what percentage a value is of total (e.g., 20 is what % of 100)",
                        "default": "of",
                    },
                },
                "required": ["value", "total"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["value", "total"])
        value = float(args["value"])
        total = float(args["total"])
        mode = args.get("mode", "of")
        
        if mode == "of":
            # Calculate value% of total
            result = (value / 100) * total
            equation = f"{value}% of {total} = {result}"
        else:  # mode == "is"
            # Calculate what % value is of total
            if total == 0:
                raise ValueError("Cannot calculate percentage when total is zero")
            result = (value / total) * 100
            equation = f"{value} is {result}% of {total}"
        
        response = {
            "operation": "percentage",
            "mode": mode,
            "value": value,
            "total": total,
            "result": result,
            "equation": equation,
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]


class ExpressionEvaluatorToolHandler(ToolHandler):
    """Evaluate a mathematical expression."""

    def __init__(self) -> None:
        super().__init__("evaluate_expression")

    def get_tool_description(self) -> Tool:
        return Tool(
            name=self.name,
            title="Evaluate Expression",
            description="Evaluate a mathematical expression string. Supports +, -, *, /, **, (), and standard math functions.",
            inputSchema={
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to evaluate (e.g., '2 + 3 * 4', 'sqrt(16) + pow(2, 3)')",
                    }
                },
                "required": ["expression"],
            },
        )

    async def run_tool(self, args: dict) -> Sequence[TextContent]:
        self.validate_required_args(args, ["expression"])
        expression = args["expression"]
        
        # Safe evaluation using math module functions
        safe_dict = {
            "sqrt": math.sqrt,
            "pow": math.pow,
            "abs": abs,
            "round": round,
            "floor": math.floor,
            "ceil": math.ceil,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "log10": math.log10,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
        }
        
        try:
            result = eval(expression, {"__builtins__": {}}, safe_dict)
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
        
        response = {
            "operation": "expression_evaluation",
            "expression": expression,
            "result": result,
        }
        
        return [TextContent(type="text", text=json.dumps(response, indent=2))]
