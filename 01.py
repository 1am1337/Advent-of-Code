import re
complete_file = None
long_list = []
left = []
right= []
dist = []
similarity_score_temp = 0
similarity_score = 0
with open("01.txt") as file:
    complete_file = file.read()
long_list = re.split(r"[\s\n]+", complete_file)
for i in range(len(long_list)):
    if i % 2:
        right.append(long_list[i])
    else:
        left.append(long_list[i])
left.sort()
right.sort()

for i in range(len(left)):
    left[i] = int(left[i])
    right[i] = int(right[i])

for i in range(len(left)):
    if left[i] > right[i]:
        dist.append(left[i]-right[i])
    elif left[i] < right[i]:
        dist.append(right[i]-left[i])
    elif left[i] == right[i]:
        pass
print(abs(sum(dist)))

for i in range(len(left)):
    similarity_score_temp = right.count(left[i]) * left[i]
    similarity_score += similarity_score_temp
print(similarity_score)