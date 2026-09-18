'''10. Daily Expense Tracker 💰

Problem:
Food, Travel, Entertainment expenses input teesukoni total daily expense calculate cheyyi.

Extra:
If total > 1000:

You exceeded today's budget!'''


Food=int(input("enter food expenses:"))
Travel=int(input("enter Travel expenses:"))
Entertainment=int(input("enter Entertainment expenses:"))

total=Food+Travel+Entertainment
print("Total Expense =",total)

if total>1000:
    print("You exceeded today's budget!")


