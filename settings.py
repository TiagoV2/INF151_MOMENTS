from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App

class SettingsPage(BoxLayout):
    def __init__(self, **kwargs):
        super(SettingsPage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        label = Label(text="App Settings", size_hint=(1, 1), height=50, font_size='30sp')
        self.add_widget(label)

        buttons_layout = BoxLayout(orientation='vertical', size_hint=(1, None), spacing=10)


        general_button = Button(text="General", size_hint=(1, None), height=50)
        buttons_layout.add_widget(general_button)

    
        account_details_button = Button(text="Account Details", size_hint=(1, None), height=50)
        buttons_layout.add_widget(account_details_button)
        

        language_button = Button(text="Language", size_hint=(1, None), height=50)
        buttons_layout.add_widget(language_button)

        notification_button = Button(text="Notifications", size_hint=(1, None), height=50)
        buttons_layout.add_widget(notification_button)

        contact_button = Button(text="Contact Us", size_hint=(1, None), height=50)
        buttons_layout.add_widget(contact_button)

        privacy_button = Button(text="Privacy", size_hint=(1, None), height=50)
        buttons_layout.add_widget(privacy_button)

        
        logout_button = Button(text="Logout", size_hint=(1, None), height=50)
        buttons_layout.add_widget(logout_button)

        share_button = Button(text="Share This App!", size_hint=(1, None), height=50)
        buttons_layout.add_widget(share_button)

        save_settings_button = Button(text="Save Settings", size_hint=(1, None), height=50)


        self.add_widget(buttons_layout)

        self.add_widget(save_settings_button)

class SettingsApp(App):
    def build(self):
        return SettingsPage()

if __name__ == '__main__':
    SettingsApp().run()
