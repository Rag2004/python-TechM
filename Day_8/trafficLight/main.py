import time

def traffic_light_simulation(cycles):
    for i in range(cycles):
        print(f"\n--- Cycle {i+1} ---")

        print("🔴 RED - Stop")
        time.sleep(3)  

        print("🟢 GREEN - Go")
        time.sleep(3)  

        print("🟡 YELLOW - Get Ready")
        time.sleep(2)  

    print("\n Simulation complete.")

if __name__ == "__main__":
    try:
        cycle = int(input("Enter the number of traffic light cycles to simulate: "))
        traffic_light_simulation(cycle)
    except ValueError:
        print("Please enter a valid number.")
