from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.clock import Clock

Builder.load_string("""<MessageWidget>:
    canvas:
        Color:
            rgb: (0.3,0.3,0.3)
        RoundedRectangle:
            size: self.size
            pos: self.pos
    size_hint: (1, None)
    height: self.minimum_height
    BoxLayout:
        size_hint: (1, None)
        orientation: 'horizontal'
        height: dp(50)
        spacing: dp(10)
        padding: dp(5)
        MessageImage:
            source: root.icon_url
            size_hint: (0.3, 1)
        Label:
            size_hint: (1, 1)
            text_size: self.width, None
            text: root.user_name
    Label:
        size_hint: (1, None)
        text: root.text
        text_size: self.width, None
        height: self.texture_size[1]

<-MessageImage>:
    canvas:
        Color:
            rgb: (1, 1, 1)
        Ellipse:
            texture: self.texture
            size: self.size
            pos: self.pos

<MessageBestWidget>:
    canvas:
        Color:
            rgb: 13/255, 15/255, 19/255
        Rectangle:
            size: self.size
            pos: self.pos
    StackLayout:
        id: layout
        height: self.minimum_height
        size_hint_y: None
""")

class MessageImage(AsyncImage):
    avatarImage = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def ohNoes(ohnoe, lol):
            def change():
                ohnoe.source = lol
                ohnoe.reload()
            Clock.schedule_del_safe(change)
        self.bind(avatarImage=ohNoes)

class MessageWidget(StackLayout):
    user_name = StringProperty('')
    text = StringProperty('')
    icon_url = StringProperty('')

class MessageBestWidget(ScrollView):
    def set_channel(self, messages):
        layout = self.ids['layout']

        print(self, messages)

        layout.clear_widgets()

        for message in messages:
            url = message.author.avatar.url.partition('?')[0]

            msg = MessageWidget(user_name=message.author.name, text=message.content, icon_url=url)

            layout.add_widget(msg)