# same as squad.py
# sort candidates method.
n = 5
candidates = [2, 3, 1, 2, 2]
result = 0

candidates.sort()

targetLevel = candidates[0]
people_in_standBy = 0
for level in candidates:
    if level > targetLevel:
        people_in_standBy = 0
        targetLevel = level
    people_in_standBy += 1
    if people_in_standBy == level:
        people_in_standBy = 0
        result += 1
print(result)
