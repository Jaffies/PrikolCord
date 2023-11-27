from kivy.uix.floatlayout import FloatLayout
from loginwidget import LoginPage
from kivy.uix.textinput import TextInput
from mainpage import MainPage
from kivy.app import App
from kivy.graphics import Color, Rectangle

class DTextInput(TextInput):
    pass


class MainWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.canvas.clear()
        with self.canvas:
            Color(49/255, 51/255, 56/255)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        def resize(_, __):
            self.rect.size = self.size
            self.rect.pos = self.pos

        self.bind(size=resize, pos=resize)

    def create_login_page(self):
        self.clear_widgets()
        login_page = LoginPage(size_hint=(1, 1))

        def remove_page(_, token):
            self.remove_widget(login_page)
            app: App = App.get_running_app()
            app.token = token
            app.connected = True
            config = app.config
            config.set('discord', 'token', token)
            config.write()

        login_page.bind(token=remove_page)
        self.add_widget(login_page)

    def create_main_page(self, guilds):
        main_page: MainPage = MainPage()

        main_page.server_widget.set_servers(guilds)
        
        self.main_page = main_page

        self.add_widget(main_page)