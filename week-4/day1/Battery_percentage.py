battery = int(input("Enter battery percentage: "))

if battery >= 80:
    print("Battery Full")

elif battery >= 30:
    print("Battery OK")

elif battery >= 10:
    print("Charge Soon")

else:
    print("Low Battery")