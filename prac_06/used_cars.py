from prac_06.car import Car


def main():
    """Demo test code to show how to use Car class."""
    # Existing code
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"{my_car}")

    # New car object - "limo"
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Limo fuel after adding 20 units: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
