from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class BoxLayoutDemoApp(App):
    def build(self):
        # Explicitly load the kv file with the correct name
        self.root = Builder.load_file("box_layout_demo.kv")
        return self.root

    def handle_greet(self):
        # Update the label with a greeting message
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        # Clear the text input and reset the label
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = "Enter your name"

if __name__ == "__main__":
    BoxLayoutDemoApp().run()

