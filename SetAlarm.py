# Script to find time to set alarm

time = float(input("Enter current time: "))
alarm_set = float(input("Hours Later: "))
print("Alarm will go off at: ", (time+alarm_set)%24)