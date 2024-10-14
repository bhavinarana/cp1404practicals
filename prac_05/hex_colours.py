# Constant dictionary containing color names and their hex codes
COLOR_TO_HEX = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin Crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Army Green": "#4b5320"
}

# Function to get the hex code using case-insensitive input
def get_hex_code(color_name):
    try:
        # Case-insensitive lookup by converting the input to title case
        return COLOR_TO_HEX[color_name.title()]
    except KeyError:
        return "Invalid color name"


# Input loop to get color names from the user
color_name = input("Enter color name: ").strip()
while color_name != "":
    # Use the function to get the hex code for the entered color name
    print(get_hex_code(color_name))
    color_name = input("Enter color name: ").strip()

print("Goodbye!")