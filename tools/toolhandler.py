"""Abstract base class for calculator tool handlers."""

from abc import ABC, abstractmethod
from collections.abc import Sequence
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
