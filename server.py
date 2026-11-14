from fastmcp import FastMCP


# Create MCP server
mcp = FastMCP("Calculator Server")




# Tool 1: Addition
@mcp.tool()
def add(a:int, b:int) -> int:
    """Add two numbers."""
    return a+b


# Tool 2: Subtraction
@mcp.tool()
def substraction(a:int, b:int) -> int:
    """Subtract two numbers"""
    return a-b

# Tool 3: Multiplication
@mcp.tool()
def multiply(a:int, b:int) -> int:
    """Multiply two numbers"""
    return a*b


# Tool 4: Division
@mcp.tool()
def divide(a:float, b:float):
    """Divide two numbers"""

    if b == 0:
        raise ValueError("Cannot divide by zero")
    

    return a/b



@mcp.resource("info://calculator")
def calculator_info() -> str:
    """Get information about the calculator."""

    return "This server supports addition, subtraction, multiplication and division."



@mcp.prompt()
def explain_calculation(a: int, b: int) -> str:
    """Generate a prompt to explain an addition."""

    return f"Explain how to calculate {a} + {b} step by step."


# Start MCP server
if __name__ == "__main__":
    mcp.run()