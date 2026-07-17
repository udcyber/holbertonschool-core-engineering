#!/usr/bin/env python3
"""Implement broadcast communication."""


import asyncio
import websockets
from websockets.exceptions import ConnectionClosed
connected_clients = set()


async def connection_handler(websocket):
    """Distribute messages to all connected clients."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                try:
                    await client.send(f"B:{message}")
                except ConnectionClosed:
                    pass
    finally:
        connected_clients.remove(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
