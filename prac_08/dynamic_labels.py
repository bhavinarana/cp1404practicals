from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Main program - Kivy app to dynamically create labels based on a list of names."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # List of names (model data)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name and add it to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            # Add the label to the "main" layout widget in the kv file
            self.root.ids.main.add_widget(temp_label)

if __name__ == "__main__":
    DynamicLabelsApp().run()
