# Hello World MCP Server Simple MCP server for practicing MCP server packaging.

### Available Tools

- **hello-world**
  - A simple tool that returns a greeting
  - Arguments:
    - `greeting` (string, required): the greeting to return 

## Installation

### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *mcp-server-fetch*.

## Configuration

### Configure for Claude.app

Add to your Claude settings:

<details>
<summary>Using docker</summary>

```json
"mcpServers": {
  "fetch": {
    "command": "docker",
    "args": ["run", "-i", "--rm", "--pull=always", "mcp/fetch"]
  }
}
```
</details>

## Debugging

You can use the MCP inspector to debug the server. For uvx installations:

```
docker run --rm -p 5173:5173 -p 3000:3000 -v /var/run/docker.sock:/var/run/docker.sock --pull=always mcp/inspector
```

## License

mcp-hello-world is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
