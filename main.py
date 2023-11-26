from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from userAthentication import verifyUser, createAccount
from kivy.uix.camera import Camera

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

class settings(Screen):
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
		sm.add_widget(settings(name="settings"))
		return sm

if __name__ == "__main__":
	Window.size = (300, 600)
	Builder.load_file("pages/login.kv")
	Builder.load_file("pages/createAccountPage.kv")
	Builder.load_file("pages/todaysPrompt.kv")
	Builder.load_file("pages/home.kv")
	Builder.load_file("pages/postImage.kv")
	Builder.load_file("pages/settings.kv")
	MomentsApp().run()

