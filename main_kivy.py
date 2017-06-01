import kivy
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

###########################################################################
#os.putenv('SDL_FBDEV', '/dev/fb1')


class MyApp(App):

    def build(self):
        Clock.schedule_once(lambda dt: self.stop(), 15)
        return Label(text='Hello world')

if __name__ == '__main__':
    MyApp().run()