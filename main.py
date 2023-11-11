
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainPage(BoxLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Button(text="Login", on_press=self.show_login))
        self.add_widget(Button(text="Create Account", on_press=self.show_create_account))

    def show_login(self, instance):
        self.clear_widgets()
        from loginPage import LoginPage
        self.add_widget(LoginPage())

    def show_create_account(self, instance):
        self.clear_widgets()
        from createAccountPage import CreateAccountPage
        self.add_widget(CreateAccountPage())

class MyApp(App):
    def build(self):
        return MainPage()

if __name__ == '__main__':
    MyApp().run()

