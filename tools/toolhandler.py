"""Abstract base class for calculator tool handlers."""

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any
from mcp.types import EmbeddedResource, ImageContent, TextContent, Tool


class ToolHandler(ABC):
    """Abstract base class for all calculator tool handlers."""

    def __init__(self, tool_name: str) -> None:
        """Initialize the tool handler.
        
        Args:
            tool_name: The name of the tool.
        """
        self.name = tool_name

    @abstractmethod
    def get_tool_description(self) -> Tool:
        """Return the MCP Tool description for this handler.
        
        Returns:
            Tool object with name, description, and input schema.
        """
        pass

    @abstractmethod
    async def run_tool(
        self, args: dict
    ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
        """Execute the tool with the given arguments.
        
        Args:
            args: Dictionary of arguments for the tool.
            
        Returns:
            Sequence of content items (text, image, or embedded resource).
        """
        pass

    def validate_required_args(self, args: dict, required_fields: list[str]) -> None:
        missing = [f for f in required_fields if f not in args]
        if missing:
            raise RuntimeError(
                f"Missing required argument(s): {', '.join(repr(m) for m in missing)}"
            )

    def parse_number(self, value: Any, field_name: str) -> float:
        if isinstance(value, bool):
            raise TypeError(
                f"Invalid type for '{field_name}': bool; expected number or numeric string"
            )
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError as exc:
                raise ValueError(
                    f"Invalid numeric value for '{field_name}': {value!r}"
                ) from exc
        raise TypeError(
            f"Invalid type for '{field_name}': {type(value).__name__}; expected number or numeric string"
        )

    def parse_integer(
        self, value: Any, field_name: str, minimum: int | None = None
    ) -> int:
        if isinstance(value, bool):
            raise TypeError(
                f"Invalid type for '{field_name}': bool; expected integer or numeric string"
            )

        integer_value: int
        if isinstance(value, int):
            integer_value = value
        elif isinstance(value, float):
            if value.is_integer():
                integer_value = int(value)
            else:
                raise ValueError(
                    f"Invalid integer value for '{field_name}': {value!r}"
                )
        elif isinstance(value, str):
            try:
                parsed_value = float(value)
            except ValueError as exc:
                raise ValueError(
                    f"Invalid numeric value for '{field_name}': {value!r}"
                ) from exc
            if not parsed_value.is_integer():
                raise ValueError(
                    f"Invalid integer value for '{field_name}': {value!r}"
                )
            integer_value = int(parsed_value)
        else:
            raise TypeError(
                f"Invalid type for '{field_name}': {type(value).__name__}; expected integer or numeric string"
            )

        if minimum is not None and integer_value < minimum:
            raise ValueError(
                f"Invalid value for '{field_name}': {integer_value} is less than minimum {minimum}"
            )

        return integer_value
