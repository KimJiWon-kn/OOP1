
import math

# ===== Exercise 1 =====
# volume of sphere with radius = 5
r = 5
volume = (4/3) * math.pi * r**3
print(volume)


# ===== Exercise 2 =====
# book price with discount and shipping

cover_price = 24.95
discount = 0.40

price_after_discount = cover_price * (1 - discount)

# shipping
first_copy = 3
additional_copy = 0.75

total_cost = price_after_discount * 60 + first_copy + (59 * additional_copy)
print(total_cost)


# ===== Exercise 3 =====
# running time

# start time: 6:52 AM
start_minutes = 6 * 60 + 52

# paces (minutes per mile)
easy_pace = 8 + 15/60
tempo_pace = 7 + 12/60

# total running time
total_run = easy_pace + 3 * tempo_pace + easy_pace

# end time
end_time = start_minutes + total_run

# convert back to hours and minutes
hours = int(end_time // 60)
minutes = int(end_time % 60)

print(hours, ":", minutes)