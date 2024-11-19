from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi with name "Hummer", 200 fuel units, and fanciness of 2
    luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive the taxi for 18 km
    luxury_taxi.drive(18)

    # Check fare calculation
    expected_fare = 48.78  # Expected fare based on the provided scenario
    actual_fare = luxury_taxi.get_fare()

    # Print details and fare
    print(luxury_taxi)
    print(f"Calculated fare: ${actual_fare:.2f}")

    # Assert to ensure fare is calculated as expected
    assert abs(actual_fare - expected_fare) < 0.01, f"Fare calculation error: expected {expected_fare}, got {actual_fare}"

if __name__ == "__main__":
    main()
