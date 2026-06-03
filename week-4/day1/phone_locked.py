'''Phone Lock System

User correct PIN = 1234

3 attempts ivvali.

Correct PIN enter chesthe:

Phone Unlocked

3 wrong attempts:

Phone Locked'''

Pin = int(input('enter pin'))
correct_pin = 1236
for attempt in range(3):
    if Pin ==correct_pin:
        print("Phone Unlocked")
        break
else:
    print("phone locked")

