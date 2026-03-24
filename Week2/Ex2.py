
import time

# get current time (seconds since epoch)
t = time.time()

# convert to integer
t = int(t)

# calculate days
days = t // 86400

# calculate remaining seconds
t = t % 86400

# calculate hours
hours = t // 3600

# remaining seconds
t = t % 3600

# calculate minutes
minutes = t // 60

# seconds left
seconds = t % 60

# print result
print(days)
print(hours, minutes, seconds)