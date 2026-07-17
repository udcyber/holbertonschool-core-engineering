#!/usr/bin/env python3
"""Module that builds a websocket client"""

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to a WebSocket server and send messages through
    an open connection."""

    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    response = await connect_and_send("ws://localhost:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
