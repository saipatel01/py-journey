'''5. Electricity Bill Checker 💡

Problem:
Units consumed input ivvali.

Rules:

First 100 units → ₹5/unit
Next 100 units → ₹7/unit
Above 200 units → ₹10/unit

Final bill calculate cheyyi.'''

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Electricity Bill =", bill)
