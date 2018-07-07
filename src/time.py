import time

time = time.time()

days = time // 86400

hours = (time % 8640) // 3600

minutes = ((time % 86400) % 3600) // 60

seconds = ((time % 86400) % 3600) % 60

print('Since epoch', days, 'days,', hours, 'hours,', minutes, 'minutes, and', seconds, 'seconds has passed.')
