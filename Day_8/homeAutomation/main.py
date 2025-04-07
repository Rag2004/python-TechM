def home_system():
    print("Welcome to Smart Home Automation System")

    try:
        temperature = float(input("Enter temperature (°C): "))
        humidity = float(input("Enter humidity (%): "))
        motion = input("Is motion detected? (yes/no): ").lower()

        print("\n--- Device Status ---")
        if temperature > 30:
            print("Fan: ON (Temperature is high)")
        else:
            print("Fan: OFF (Temperature is normal)")

        if humidity > 70:
            print("Dehumidifier: ON (Humidity is high)")
        else:
            print("Dehumidifier: OFF (Humidity is acceptable)")

        if motion == "yes":
            print("Light: ON (Motion detected)")
        else:
            print("Light: OFF (No motion)")

    except ValueError:
        print("Invalid input. Please enter numeric values for temperature and humidity.")

if __name__ == "__main__":
    home_system()
