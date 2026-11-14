import asyncio

from fastmcp import Client
from server import mcp 


async def main():

    async with Client(mcp) as client:

        tools = await client.list_tools()

        print("Available MCP Tools.")

        for tool in tools:
            print(tool.name)

        
        result = await client.call_tool(
            "add",
            {
                "a":10,
                "b":20
            }
        )

        print("\nAddition Result:")
        print(result.data)


        result = await client.call_tool(
            "multiply",
            {

                "a": 5,
                "b": 4
            }
        )

        print("\nMultiplication Result:")
        print(result.data)


if __name__ == "__main__":
    asyncio.run(main())