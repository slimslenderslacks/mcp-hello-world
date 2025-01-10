from typing import Annotated, Tuple
from urllib.parse import urlparse, urlunparse

from mcp.shared.exceptions import McpError
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    GetPromptResult,
    Prompt,
    PromptArgument,
    PromptMessage,
    TextContent,
    Tool,
    INVALID_PARAMS,
    INTERNAL_ERROR,
)
from pydantic import BaseModel, Field, AnyUrl

DEFAULT_USER_AGENT_AUTONOMOUS = "ModelContextProtocol/1.0 (Autonomous; +https://github.com/modelcontextprotocol/servers)"
DEFAULT_USER_AGENT_MANUAL = "ModelContextProtocol/1.0 (User-Specified; +https://github.com/modelcontextprotocol/servers)"


async def serve() -> None:
    """Run the hello world MCP server.
    """
    server = Server("mcp-hello-world")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="hello-world",
                description="A simple tool that returns a greeting.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "greeting": {
                            "type": "string",
                            "description": "The greeting to return.",
                        }
                    },
                    "required": ["timezone"],
                },
            )
        ]

    @server.call_tool()
    async def call_tool(name, arguments: dict) -> list[TextContent]:

        return [TextContent(type="text", text=f"{arguments['greeting']} World!")]

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options, raise_exceptions=True)
