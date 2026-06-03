current_time = int(input("Enter current time: "))
alarm_time = int(input("Enter alarm time: "))

hours_left = alarm_time - current_time

if hours_left <= 0:
    hours_left += 24

print("Alarm will ring in", hours_left, "hours")