import random
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require("2.0.0")


class GameView(BoxLayout):
    def __init__(self):
        super(GameView, self).__init__()
        self.randomValue = random.randint(0, 1000)

    def check_number(self):
        if int(self.answer_input.text) == self.randomValue:
            self.result_label.text = "Victoire !!!"
            self.result_label.color = "#00EF0B"
        elif int(self.answer_input.text) > self.randomValue:
            self.result_label.text = "Less"
            self.result_label.color = "#EF3E00"
        elif int(self.answer_input.text) < self.randomValue:
            self.result_label.text = "More"
            self.result_label.color = "#EF3E00"


class MobApp(App):
    def build(self):
        return GameView()


mobApp = MobApp()
mobApp.run()
