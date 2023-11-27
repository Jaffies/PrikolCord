from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.stacklayout import StackLayout
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty
from kivy.app import App
from discord import TextChannel
from kivy.uix.button import Button
from kivy.clock import Clock
from functools import partial

Builder.load_string("""<ServerWidget>:
    orientation: 'horizontal'
    canvas:
        Color:
            rgb: 30/255, 31/255, 34/255
        Rectangle:
            size: self.size
            pos: self.pos
    ScrollView:
        size_hint_x: 0.2
        GuildWidget:
            spacing: '8dp'
            size_hint_y: None
            height: self.minimum_height
            id: guild
    ChannelWidget:
        id: channel
    
<-CircleImage>:
    size_hint: (1, None)
    height: self.width
    canvas:
        Color:
            rgb: (1, 1, 1)
        Ellipse:
            texture: self.texture
            size: self.size
            pos: self.pos

<ChannelWidget>:
    orientation: 'vertical'
    spacing: '10sp'
    canvas:
        Color:
            rgb: 43/255, 45/255, 49/255
        RoundedRectangle:
            size: self.size
            pos: self.pos
    Label:
        bold: True
        size_hint: (1, 0.1)
        font_size: '20dp'
        text_size: self.size
        halign: 'center'
        valign: 'center'
        id: label
    ScrollView:
        StackLayout:
            size_hint: 1, None
            spacing: '10sp'
            height: self.minimum_height
            id: layout

<ChannelButton>:
    size_hint: (1, None)
    font_size: '15sp'
    text_size: self.width, None
    height: self.texture_size[1]
    background_color: (1,1,1,0)
    foreground_color: (128/255, 132/255, 142/255)
""")


class GuildWidget(StackLayout):
    pass


class CircleImage(AsyncImage):
    guild_id = NumericProperty(0)

    def __init__(self, **kwargs):
        if 'source' in kwargs:
            kwargs['source'] = kwargs['source'].partition('?')[0]

        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            App.get_running_app().discord_client.set_server.start(self.guild_id)
        return False


class ServerWidget(BoxLayout):
    def set_servers(self, guilds):
        guild_widget: GuildWidget = self.ids['guild']
        guild_widget.clear_widgets()

        for guild in guilds:
            icon = guild.icon
            url = icon.url.partition('?')[0]

            def lol(url, id, _):
                circle = CircleImage(source=url, guild_id=id)
                guild_widget.add_widget(circle)

            Clock.schedule_once(partial(lol, url, guild.id))

    def set_server(self, guild):
        channel = self.ids['channel']
        label = channel.ids['label']

        label.text = guild.name

        layout: StackLayout = channel.ids['layout']

        layout.clear_widgets()

        for channel in guild.channels:
            if not isinstance(channel, TextChannel):
                continue

            if not channel.permissions_for(guild.me).read_message_history:
                continue

            button = ChannelButton(channel_id=channel.id, text=channel.name)

            layout.add_widget(button)


class ChannelButton(Button):
    channel_id = NumericProperty(0)

    def on_press(self):
        app = App.get_running_app()
        app.discord_client.set_channel.start(self.channel_id)


class ChannelWidget(BoxLayout):
    pass
