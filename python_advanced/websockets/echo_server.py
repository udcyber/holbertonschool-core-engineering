#!/usr/bin/env python3
"""Build a WebSocket server."""

import asyncio
import websockets


async def connection_handler(websocket):
    """Sends back the message a client sends."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
