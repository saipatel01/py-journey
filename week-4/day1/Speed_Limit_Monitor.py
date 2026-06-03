'''7. Speed Limit Monitor 🚗

Problem:
Vehicle speed input ivvali.

Rules:

≤60 → Safe
61–80 → Warning

80 → Overspeeding'''


speed=int(input("enter speed of vehicle: "))

if speed<=60:
    print("Safe")
elif speed < 80:
    print("Warning")
else:
    print("overspeeding")