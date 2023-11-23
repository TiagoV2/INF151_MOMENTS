from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from userAthentication import verifyUser, createAccount

class MomentsLogin(Screen):
	def login(self, userName, password):
		if verifyUser(userName, password):
			self.manager.current = "todaysPrompt"
		else:
			print("Invalid working")

class MomentsCreateAccount(Screen):
	def createAccount(self, userName, password, reEnteredPassword):
		if password == reEnteredPassword and createAccount(userName, password):
			self.manager.current = "todaysPrompt"
		else:
			print("Not new User or password != reEnteredPassword")
			

class todaysPrompt(Screen):
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
		return sm

if __name__ == "__main__":
	Window.size = (300, 600)
	Builder.load_file("login.kv")
	Builder.load_file("createAccountPage.kv")
	Builder.load_file("todaysPrompt.kv")
	MomentsApp().run()

