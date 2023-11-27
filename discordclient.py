from kivy.app import App
from server_widget import CircleImage
import discord.ext.tasks


def update_servers(widget, guilds):
    widget.server_widget.set_servers(guilds)


class DiscordClient(discord.Client):
    app: App

    @discord.ext.tasks.loop(count=1)
    async def set_server(self, guild):
        print(self, self.get_guild(guild))
        self.app.root.main_page.server_widget.set_server(self.get_guild(guild))

    @discord.ext.tasks.loop(count=1)
    async def set_channel(self, channel_id):
        channel = self.get_channel(channel_id)
        lst = []
        print(channel, 'start history lol')
        async for message in channel.history(limit=50):
            print('message', message)
            lst.append(message)
        print(lst)
        self.app.root.main_page.messages_widget.set_channel(lst)

    async def on_ready(self):
        print('logged in', self.user)
        self.app.root.create_main_page(self.guilds)

    async def on_guild_join(self, guild):
        print('oh noes')
        server_widget = self.app.root.main_page.server_widget

        circle = CircleImage(source=guild.icon.url, guild_id=guild.id)

        server_widget.ids['guild'].add_widget(circle)

    async def on_guild_remove(self, guild):
        server_widget = self.app.root.main_page.server_widget
        guilds = server_widget.ids['guild']

        for widget in guilds.children:
            if widget.guild_id == guild.id:
                guilds.remove_widget(widget)
                break
