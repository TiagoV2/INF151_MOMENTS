
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from userAthentication import verifyUser, createAccount
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class MomentsLogin(Screen):
	def login(self, userName, password):
		if verifyUser(userName, password):
			self.manager.current = "todaysPrompt"
		# add a pop up message to help the user

class MomentsCreateAccount(Screen):
	def createAccount(self, userName, password, reEnteredPassword):
		if password == reEnteredPassword and createAccount(userName, password):
			self.manager.current = "todaysPrompt"
		# add a pop up to help the user understand
			

class todaysPrompt(Screen):
	pass

class home(Screen):
	pass

class postImage(Screen):
	def capture(self):
		self.ids.cam.export_to_png("photo.png")
		self.manager.current = "postFinalImage" #goes to next page


class postFinalImage(Screen):
    def on_enter(self):
        self.deactivate_camera()
        image = Image(source='photo.png', size_hint=(1, 0.8))

        
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        post_button = Button(text='Post Image', on_press=self.post_image, size_hint_x=0.5)
        add_images_button = Button(text='Add Images', on_press=self.add_images, size_hint_x=0.5)

        buttons_layout.add_widget(post_button)
        buttons_layout.add_widget(add_images_button)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(image)
        layout.add_widget(buttons_layout)
        self.add_widget(layout)

    def deactivate_camera(self):
        if hasattr(self.ids, 'cam') and hasattr(self.ids.cam, 'active'):
            self.ids.cam.active = False

    def post_image(self, instance):
        self.show_popup("Image Posted!")

    def add_images(self, instance):
        self.show_popup("Add Images clicked!")

    def show_popup(self, message):
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text=message))
        popup = Popup(title='Info', content=popup_content, size_hint=(None, None), size=(400, 200))
        popup.open()


class settings(Screen):
	pass

class general(Screen):
	pass

class accountDetails(Screen):
	pass

class language(Screen):
	pass

class accessibility(Screen):
	pass

class privacy(Screen):
	pass

class WindowManager(ScreenManager):
	pass


class MomentsApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "DeepOrange"
		sm = WindowManager()
		sm.add_widget(MomentsLogin(name='login'))
		sm.add_widget(MomentsCreateAccount(name='createAccount'))
		sm.add_widget(todaysPrompt(name="todaysPrompt"))
		sm.add_widget(home(name="home"))
		sm.add_widget(postImage(name="postImage"))
		sm.add_widget(postFinalImage(name="postFinalImage"))
		sm.add_widget(settings(name="settings"))
		sm.add_widget(general(name="general"))
		sm.add_widget(accountDetails(name="accountDetails"))
		sm.add_widget(language(name="language"))
		sm.add_widget(privacy(name="privacy"))
		sm.add_widget(accessibility(name="accessibility"))
		return sm

if __name__ == "__main__":
	Window.size = (300, 600)
	Builder.load_file("pages/login.kv")
	Builder.load_file("pages/createAccountPage.kv")
	Builder.load_file("pages/todaysPrompt.kv")
	Builder.load_file("pages/home.kv")
	Builder.load_file("pages/postImage.kv")
	Builder.load_file("pages/postFinalImage.kv")
	Builder.load_file("pages/settings.kv")
	Builder.load_file("pages/general.kv")
	Builder.load_file("pages/accountDetails.kv")
	Builder.load_file("pages/accessibility.kv")
	Builder.load_file("pages/privacy.kv")
	
	MomentsApp().run()

