from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class PromptApp(App):
    def build(self):
        layout = RelativeLayout(size=(400, 600))

        # Today's Prompt Label
        prompt_label = Label(
            text="Today's Prompt",
            size_hint=(None, None),
            size=(400, 100),
            pos_hint={'center_x': 0.5, 'top': 1},
            font_size='30sp'
        )
        layout.add_widget(prompt_label)

        # Lorem Ipsum Text Prompt
        lorem_ipsum_text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
        prompt_text_label = Label(
            text=lorem_ipsum_text,
            size_hint=(None, None),
            size=(400, 200),
            pos_hint={'center_x': 0.5, 'top': 0.8},
            font_size='20sp'
        )
        layout.add_widget(prompt_text_label)

        # Add Picture Button
        add_picture_button = Button(
            text="Add Picture",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'top': 0.4},
        )
        layout.add_widget(add_picture_button)

        # Camera Icon
        # camera_icon = Image(
        #     source="https://i.pinimg.com/736x/f9/cf/20/f9cf2024b2b7596b8b8f4bf0f00c055a.jpg",
        #     size_hint=(None, None),
        #     size=(50, 50),
        #     pos_hint={'left': 0.1, 'top': 0.7}
        # )
        layout.add_widget(camera_icon)

        # Lock Button
        lock_button = Button(
            text="Lock",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'right': 0.95, 'bottom': 0.05},
        )
        layout.add_widget(lock_button)

        return layout

if __name__ == '__main__':
    PromptApp().run()
