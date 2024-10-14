from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

def read_file(filename):
    """Read the data file and return a list of lists, where each list represents a row of data."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header line
        for line in in_file:
            data.append(line.strip().split('\t'))  # Split by tabs
    return data

def count_champion_wins(data):
    """Count how many times each champion has won."""
    champion_wins = {}
    for row in data:
        champion = row[2]  # The champion's name is in the third column
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
    return champion_wins

def get_champion_countries(data):
    """Return a set of the countries of champions."""
    countries = set()
    for row in data:
        country = row[1]  # The champion's country is in the second column
        countries.add(country)
    return sorted(countries)

class WimbledonApp(App):
    def build(self):
        # Create a main layout
        layout = BoxLayout(orientation='vertical', padding=10)

        # Add a button to display champions
        btn_show_champions = Button(text="Show Champions", size_hint=(1, 0.2))
        btn_show_champions.bind(on_press=self.show_champions)
        layout.add_widget(btn_show_champions)

        # Add a button to display countries
        btn_show_countries = Button(text="Show Countries", size_hint=(1, 0.2))
        btn_show_countries.bind(on_press=self.show_countries)
        layout.add_widget(btn_show_countries)

        # Create a label to display output
        self.output_label = Label(size_hint=(1, 0.6))
        layout.add_widget(self.output_label)

        # Read the data
        self.data = read_file("wimbledon_data.txt")
        return layout

    def show_champions(self, instance):
        champion_wins = count_champion_wins(self.data)
        champions_str = "Wimbledon Champions:\n"
        for champion, wins in sorted(champion_wins.items(), key=lambda x: x[0]):
            champions_str += f"{champion} {wins}\n"
        self.output_label.text = champions_str

    def show_countries(self, instance):
        champion_countries = get_champion_countries(self.data)
        countries_str = "Countries that have won Wimbledon:\n" + ", ".join(champion_countries)
        self.output_label.text = countries_str

if __name__ == "__main__":
    WimbledonApp().run()