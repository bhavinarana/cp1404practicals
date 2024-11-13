from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# Conversion factor
MILES_TO_KM = 1.60934

class ConvertMilesApp(App):
    km_text = StringProperty("0.0 km")

    def build(self):
        # Explicitly load the correct kv file
        self.root = Builder.load_file("convert_miles.kv")
        return self.root

    def update_km(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * MILES_TO_KM
            self.km_text = f"{km:.2f} km"
        except ValueError:
            self.km_text = "0.0 km"

    def handle_increment(self, change):
        try:
            miles = float(self.root.ids.input_miles.text) if self.root.ids.input_miles.text else 0
        except ValueError:
            miles = 0
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.update_km()

if __name__ == "__main__":
    ConvertMilesApp().run()

