
# ===== Exercise 1 =====
minutes = 42
seconds = 42

total_seconds = minutes * 60 + seconds
print(total_seconds)


# ===== Exercise 2 =====
kilometers = 10
miles = kilometers / 1.61

print(miles)


# ===== Exercise 3 =====
# total time in seconds
time_seconds = 42 * 60 + 42

# convert time to hours
time_hours = time_seconds / 3600

# distance in miles
distance_miles = 10 / 1.61

# average speed (miles per hour)
speed = distance_miles / time_hours
print(speed)

# pace (time per mile)
pace = time_seconds / distance_miles

pace_minutes = int(pace // 60)
pace_seconds = int(pace % 60)

print(pace_minutes, "minutes", pace_seconds, "seconds per mile")