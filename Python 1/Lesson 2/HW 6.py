import math

record_seconds = float(input())
distance_meters = float(input())
time_per_meter = float(input())

base_time = distance_meters * time_per_meter

resistance_count = math.floor(distance_meters / 15)
resistance_time = resistance_count * 12.5

total_time = base_time + resistance_time

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - record_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")