# clock displays number in format of HH:MM:SS
# how many times, that are including target numbers are in clock?
# time arrange is 00:00:00 ~ targetNumber:MM:SS
# hours could be 0 ~ 23
# minutes could be 0 ~ 59
# seconds could be 0 ~ 59
# how many target number could come in hours? no restrictions
# how many target number could come in minutes? no target number in hours.
# how many target number could come in seconds? only in seconds.
target_number = 3
max_hours = 23
max_minutes = 59
max_seconds = 59
case1 = 0
case2 = 0
case3 = 0

if target_number >= 3:
    case1 = 1
else:
    case1 = 3 + 9 + 9
case1 *= max_minutes * max_seconds

if target_number >= 6:
    case2 = 1
else:
    case2 = 6 * 9
case2 *= (max_seconds + 1)
case2 = 3 + 9 + 9

if target_number >= 6:
    case3 = 1
else:
    case3 = 6*9

result = case1 + case2 + case3
print(result)
