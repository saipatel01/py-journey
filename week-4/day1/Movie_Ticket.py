'''6. Movie Ticket Eligibility 🎬

Problem:
Age input teesukoni ticket type cheppali.

Rules:

Below 5 → Free Entry
5–17 → Child Ticket
18–59 → Adult Ticket
60+ → Senior Citizen Ticket'''

Age=int(input("Enter Age: "))
if Age<5:
    print("Free Entry")
elif Age<=17:
    print("child ticket")
elif Age <=59:
    print("Adult Ticket")
else:
   print("Senoir Citizen Ticket")


