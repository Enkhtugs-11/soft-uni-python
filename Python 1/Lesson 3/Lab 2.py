day = input()
switch_days = {
    "Monday": "Working day",
    "Tuesday": "Working day",
    "Wednesday": "Working day",
    "Thursday": "Working day",
    "Friday": "Working day",
    "Saturday": "Weekend",
    "Sunday": "Weekend",
}
print(switch_days.get(day,"Error"))
