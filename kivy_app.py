from kivy.app import App
from kivy.config import ConfigParser
from discordclient import DiscordClient
from kivy.core.window import Window
from mainwidget import MainWidget
from kivy.properties import BooleanProperty, StringProperty

Window.size = (324, 720)
Window.title = 'PrikolCord'
Window.resizable = False

class PrikolCordApp(App):
    connected = BooleanProperty(False)
    token = StringProperty('')
    client: DiscordClient

    def build(self):
        config: ConfigParser = self.config
        self.token = config.get('discord', 'token')

        root = MainWidget()


        if self.token == '':
            root.create_login_page()
        else:
            self.connected = True

        return root

    def build_config(self, config: ConfigParser):
        config.adddefaultsection('discord')
        config.setdefault('discord', 'token', '')
