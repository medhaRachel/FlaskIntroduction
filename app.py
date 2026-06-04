import asyncio
import aiohttp

async def handle_request():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://external-api.com/data') as response:
            return await response.json()