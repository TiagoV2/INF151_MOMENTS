from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CreateAccountPage(BoxLayout):
    def __init__(self, **kwargs):
        super(CreateAccountPage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Moments"))

        self.email_input = TextInput(hint_text="Email")
        self.password_input = TextInput(hint_text="Password", password=True)
        self.confirm_password_input = TextInput(hint_text="Confirm Password", password=True)
        
        self.add_widget(self.email_input)
        self.add_widget(self.password_input)
        self.add_widget(self.confirm_password_input)

        create_account_button = Button(text="Create Account", size_hint=(None, None), height=50)
        self.add_widget(create_account_button)

