#!/usr/bin/env python3
"""Module that builds a websocket client"""

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to a WebSocket server and send messages through
    an open connection and return the response."""

    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    response = await connect_and_send("ws://127.0.0.1:8765", "Hello WebSocket")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
