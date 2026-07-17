#!/usr/bin/env python3
"""Manage multiple connected clients and
control how messages are delivered."""


import asyncio
import websockets
from websockets.exceptions import ConnectionClosed
connected_clients = set()


async def connection_handler(websocket):
    """Manage multiple connected clients."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
