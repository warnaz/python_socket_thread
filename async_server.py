import asyncio
from utils import port, host


async def handle_client(reader, writer):
    request = None
    while request != 'quit':
        request = (await reader.read(255)).decode('utf8')
        print('Request: ', request)
        response = str(eval(request)) + '\n'
        writer.write(response.encode('utf8'))
        await writer.drain()
    writer.close()


async def run_server():
    server = await asyncio.start_server(handle_client, host, port)
    async with server:
        await server.serve_forever()


asyncio.run(run_server())
