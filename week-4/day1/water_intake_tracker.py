water=float(input("enter water taken:"))
goal=3
left = goal-water
if goal  > water:
    print("need",left,"more liters")
else:
    print("goal achived")