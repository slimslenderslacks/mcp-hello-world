from .server import serve

def main():
    """MCP Hello World"""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="give a model the ability to run a function"
    )

    args = parser.parse_args()
    asyncio.run(serve())


if __name__ == "__main__":
    main()
