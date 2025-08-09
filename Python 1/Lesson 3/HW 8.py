exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_total = exam_hour * 60 + exam_minute
arrival_total = arrival_hour * 60 + arrival_minute

diff = arrival_total - exam_total

if diff > 0:
    print("Late")
elif diff >= -30:
    print("On time")
else:
    print("Early")

if diff != 0:
    abs_diff = abs(diff)
    hours = abs_diff // 60
    minutes = abs_diff % 60

    if hours == 0:
        if diff < 0:
            print(f"{minutes} minutes before the start")
        else:
            print(f"{minutes} minutes after the start")
    else:
        if diff < 0:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{hours}:{minutes:02d} hours after the start")
