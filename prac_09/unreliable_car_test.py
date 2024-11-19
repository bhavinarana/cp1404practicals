from prac_09.unreliable_car import UnreliableCar

def main():
    # Create instances of UnreliableCar with different reliabilities
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)  # 90% chance to drive
    unreliable_car = UnreliableCar("Mostly Unreliable", 100, 10)  # 10% chance to drive

    # Try to drive each car a set distance multiple times and print results
    print("Testing Mostly Reliable Car (90% reliability):")
    for i in range(5):
        distance_driven = reliable_car.drive(20)
        print(f"Attempt {i+1}: Drove {distance_driven} km")

    print("\nTesting Mostly Unreliable Car (10% reliability):")
    for i in range(5):
        distance_driven = unreliable_car.drive(20)
        print(f"Attempt {i+1}: Drove {distance_driven} km")

if __name__ == "__main__":
    main()
