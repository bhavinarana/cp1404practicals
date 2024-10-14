

# Function to extract the name from the email
def extract_name_from_email(email):
    prefix = email.split('@')[0] 
    parts = prefix.split('.')    
    name = ' '.join(parts).title()  
    return name

# Main program
emails = {}

email = input("Email: ").strip()
while email != "":
    # Extract name from the email
    name = extract_name_from_email(email)

    # Ask the user if the extracted name is correct
    is_name_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

    # If the user enters something other than "Y" or "yes", ask for their name
    if is_name_correct not in ('', 'y', 'yes'):
        name = input("Name: ").strip()

    # Store the email and name in the dictionary
    emails[email] = name

    # Ask for the next email
    email = input("Email: ").strip()

# Print the collected emails and names
print("\nCollected Emails and Names:")
for email, name in emails.items():
    print(f"{name} ({email})"