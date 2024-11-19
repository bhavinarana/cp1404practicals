from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display all available taxis with their details."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Prompt the user to choose a taxi and return the selected taxi, or None if invalid."""
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input; please enter a number.")
    return None


def drive_taxi(current_taxi, total_cost):
    """Drive the selected taxi, calculate the fare, and update the total cost."""
    try:
        distance = int(input("Drive how far? "))
        actual_distance = current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        total_cost += trip_cost
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        current_taxi.start_fare()  # Reset fare distance for the next trip
    except ValueError:
        print("Invalid input; please enter a number.")
    return total_cost


def main():
    """Taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_cost = 0.0
    choice = ""

    print("Let's drive!")

    while choice != "q":
        print("\nq)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "c":
            selected_taxi = choose_taxi(taxis)
            if selected_taxi:
                current_taxi = selected_taxi
                print(f"You chose: {current_taxi}")
            print(f"Bill to date: ${total_cost:.2f}")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_cost = drive_taxi(current_taxi, total_cost)
            print(f"Bill to date: ${total_cost:.2f}")

        elif choice != "q":
            print("Invalid option")
            print(f"Bill to date: ${total_cost:.2f}")

    # End of program summary
    print(f"\nTotal trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == "__main__":
    main()
