from kivy.app import App
from kivy.lang import Builder

CONVERSION_FACTOR = 1.609


class ConvertMileskm(App):
    def build(self):
        self.title = "ConvertMilesKm"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, increment):
        try:
            if self.root.ids.input_miles.text == '':
                self.root.ids.input_miles.text = '0'
            self.root.ids.input_miles.text = str(int(self.root.ids.input_miles.text) + increment)
        except ValueError:
            print("Invalid Miles Value")

    def handle_convert(self):
        try:
            self.root.ids.output_label.text = str(CONVERSION_FACTOR * int(self.root.ids.input_miles.text))
        except ValueError:
            print("Invalid Miles Value")
            self.root.ids.input_miles.text = ''


ConvertMileskm().run()
