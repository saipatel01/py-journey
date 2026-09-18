'''
Game Rules
1. There are two players: you and your opponent.
2. Players take turns picking up one coin at a time.
3. You always make the first move.
4. The player who picks the last coin wins.
'''

coins=int(input("enter number : 53"))
print("winner is:" , end = "")
if coins % 2 == 0:
    print("Opponent")
else:
    print("U")


