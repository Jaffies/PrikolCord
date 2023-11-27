from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

from messages_widget import MessageBestWidget
from server_widget import  ServerWidget

class ServerLayout():
    pass

class MainPage(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.server_widget = ServerWidget()

        self.add_widget(self.server_widget)

        self.messages_widget = MessageBestWidget()

        self.add_widget(self.messages_widget)

        #users_widget = Button()

        #self.add_widget(users_widget)

        self.border = self.border*0.5
