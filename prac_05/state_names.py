"""
CP1404/CP5632 Practical
State names in a dictionary
File reformatted following PEP 8 standards
"""

# Dictionary of state abbreviations and full state names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Function to get the state name using EAFP
def get_state_name(state_code):
    try:
        # Return the state name, handling both uppercase and lowercase inputs
        return CODE_TO_NAME[state_code.upper()]
    except KeyError:
        return "Invalid short state"

# Print all states and names neatly aligned
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

# Input loop to get state codes from the user
state_code = input("Enter short state: ").strip()
while state_code != "":
    # Use the function to get the state name using the EAFP approach
    print(get_state_name(state_code))
    state_code = input("Enter short state: ").strip()