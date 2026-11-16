def physics_operations():
    print("\n===== PHYSICS OPERATIONS =====")
    print("1. Calculate Speed")
    print("2. Calculate Acceleration")
    print("3. Calculate Force")
    print("4. Calculate Momentum")
    print("5. Calculate Work Done")
    print("6. Calculate Power")
    print("7. Calculate Density")

    choice = int(input("Select an operation (1-7): "))

    if choice == 1:
        distance = float(input("Enter distance (m): "))
        time = float(input("Enter time (s): "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            print("Speed =", distance / time, "m/s")

    elif choice == 2:
        final_velocity = float(input("Enter final velocity (m/s): "))
        initial_velocity = float(input("Enter initial velocity (m/s): "))
        time = float(input("Enter time (s): "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            print("Acceleration =", (final_velocity - initial_velocity) / time, "m/s²")

    elif choice == 3:
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s²): "))
        print("Force =", mass * acceleration, "N")

    elif choice == 4:
        mass = float(input("Enter mass (kg): "))
        velocity = float(input("Enter velocity (m/s): "))
        print("Momentum =", mass * velocity, "kg·m/s")

    elif choice == 5:
        force = float(input("Enter force (N): "))
        distance = float(input("Enter distance (m): "))
        print("Work done =", force * distance, "J")

    elif choice == 6:
        work = float(input("Enter work done (J): "))
        time = float(input("Enter time (s): "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            print("Power =", work / time, "W")

    elif choice == 7:
        mass = float(input("Enter mass (kg): "))
        volume = float(input("Enter volume (m³): "))
        if volume == 0:
            print("Volume cannot be zero.")
        else:
            print("Density =", mass / volume, "kg/m³")

    else:
        print("Invalid choice. Please select a number from 1 to 7.")


while True:
    physics_operations()
    again = input("\nDo you want to continue? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thank you for using the Physics Operations Program!")
        break
