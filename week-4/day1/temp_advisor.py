'''9. Temperature Advisor 🌡️

Problem:
Temperature input teesukoni suggestion ivvali.

Rules:

<15 → Wear Jacket
15–30 → Pleasant Weather

30 → Stay Hydrated'''

temp=int(input("enter temperature:"))
if temp < 15:
    print("wear Jacket")
elif temp <30:
    print("Pleasant water")
else:
    print("stay Hyderated")
