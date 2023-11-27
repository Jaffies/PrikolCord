import os
os.environ["KIVY_NO_CONSOLELOG"] = '0'

from kivy_app import PrikolCordApp
import asyncio
from discordclient import DiscordClient
from discord.errors import LoginFailure


async def run_app(prikolCord: PrikolCordApp, discordTask: asyncio.Task):

    await prikolCord.async_run(async_lib='asyncio')
    discordTask.cancel()

async def discord_think(discordClient: DiscordClient, app: PrikolCordApp):
    try:
        while not app.connected:
            await asyncio.sleep(0.1)
        await discordClient.start(app.token)
    except asyncio.CancelledError:
        pass
    except LoginFailure:
        app.token = ''
        app.root.create_login_page()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app = PrikolCordApp()
    client = DiscordClient()

    app.discord_client = client
    client.app = app

    future = asyncio.ensure_future(discord_think(client, app))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(run_app(app, future), future))
    loop.close()
