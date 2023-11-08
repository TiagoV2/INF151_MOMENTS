from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Moments"))
        
        self.email_input = TextInput(hint_text="Email")
        self.password_input = TextInput(hint_text="Password", password=True)
        
        self.add_widget(self.email_input)
        self.add_widget(self.password_input)

        login_button = Button(text="Login", size_hint=(None, None), height=50)
        self.add_widget(login_button)


