# n is number of candidates.
# x is fear sensitivity level.
# group as many squad as possible, some can be left out.
# person with x fear sensitivity should be in group with x people in. (including own self).
n = 5
candidates = [2, 3, 1, 2, 2]
possible_candidates = {}
result = 0

unique_fear_level = set(candidates)

for level in unique_fear_level:
    peopleWithLevel = candidates.count(level)
    if level <= peopleWithLevel:
        possible_candidates[level] = peopleWithLevel

for level in possible_candidates:
    result += possible_candidates[level] // level

print(result)
