import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8

rest_time = break_duration / 4

remaining_time = break_duration - lunch_time - rest_time

if remaining_time >= episode_duration:
    free_time = math.ceil(remaining_time - episode_duration)
    print(f"You have enough time to watch {series_name} and left with {free_time} minutes free time.")
else:
    needed_time = math.ceil(episode_duration - remaining_time)
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")
