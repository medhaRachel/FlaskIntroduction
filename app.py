import asyncio
import aiohttp

async def fetch_data(session):
    async with session.get('http://external-api.com/data') as response:
        return await response.json()

async def handle_request_async():
    async with aiohttp.ClientSession() as session:
        data = await fetch_data(session)
        return render_template('result.html', data=data)

def handle_request():
    return asyncio.run(handle_request_async())