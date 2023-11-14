from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.camera import Camera
import cv2
import time

from kivy.lang import Builder

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")

        # Access the camera frames using OpenCV
        frame = camera.texture.pixels
        frame = cv2.flip(frame, 0)  # Flip vertically (OpenCV uses different axis)
        cv2.imwrite(f"IMG_{timestr}.png", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        print("Captured")


class TestCamera(App):
    def build(self):
        return CameraClick()


if __name__ == '__main__':
    TestCamera().run()
