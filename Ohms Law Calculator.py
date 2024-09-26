def ohms_law_calculator():
    print("Ohm's Law Calculator")
    print("1. Calculate Voltage (V)")
    print("2. Calculate Current (I)")
    print("3. Calculate Resistance (R)")
    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        current = float(input("Enter current (I) in amps: "))
        resistance = float(input("Enter resistance (R) in ohms: "))
        if resistance == 0:
            print("Error: Resistance cannot be zero!")
        else:
            voltage = current * resistance
            print(f"Voltage (V) = {voltage} volts")
    elif choice == 2:
        voltage = float(input("Enter voltage (V) in volts: "))
        resistance = float(input("Enter resistance (R) in ohms: "))
        if resistance == 0:
            print("Error: Resistance cannot be zero!")
        else:
            current = voltage / resistance
            print(f"Current (I) = {current} amps")
    elif choice == 3:
        voltage = float(input("Enter voltage (V) in volts: "))
        current = float(input("Enter current (I) in amps: "))
        if current == 0:
            print("Error: Current cannot be zero!")
        else:
            resistance = voltage / current
            print(f"Resistance (R) = {resistance} ohms")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ohms_law_calculator()