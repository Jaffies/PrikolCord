from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class DTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (30/255, 31/255, 34/255)
        self.cursor_color = (1, 1, 1)
        self.foreground_color = (1, 1, 1, 1)
        self.hint_text_color = (122/255, 128/255, 136/255, 1)
        self.multiline = False
        self.font_size = '16sp'
        self.background_normal = ''


class DButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (88/255, 101/255, 242/255)
        self.background_normal = ''
