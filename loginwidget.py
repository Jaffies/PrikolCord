from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from discord_widgets import DTextInput, DButton
from kivy.properties import StringProperty


class LoginPage(FloatLayout):
    token = StringProperty('')
    rect: Rectangle

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.canvas.clear()
        with self.canvas:
            Color(49/255, 51/255, 56/255)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        label = Label(text='Login',
                      pos_hint={'center_y': 0.9, 'center_x': 0.5},
                      font_size='20sp',
                      bold=True)
        self.add_widget(label)

        textinput = DTextInput(size_hint=(0.8333, 0.05),
                               pos_hint={'center_x': 0.5, 'center_y': 0.8},
                               hint_text='Token'
                               )
        self.add_widget(textinput)

        button = DButton(size_hint=(0.833, 0.05),
                         pos_hint={'center_x': 0.5, 'center_y': 0.7},
                         text='Continue'
                         )

        def connect(_):
            text = textinput.text

            if text == '':
                return

            self.token = text

        button.bind(on_press=connect)
        self.add_widget(button)

        def redraw(_, __):
            self.rect.size = self.size
            self.rect.pos = self.pos

        self.bind(pos=redraw, size=redraw)
