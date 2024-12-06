import re
complete_file = None
safe_reports = []
safe_reports_temp = []
with open("02test.txt") as file:
    complete_file = file.read()

lines = complete_file.split("\n")
for i in range(len(lines)):
    lines[i] = lines[i].split(" ")

for i in range(len(lines)):
    if lines[i] == sorted(lines[i]):
        safe_reports_temp.append(lines[i])
    elif lines[i] == sorted(lines[i], reverse = True):
        safe_reports_temp.append(lines[i])
    else:
        pass # report is unsafe

for i in range(len(safe_reports_temp)):
    for j in range(len(safe_reports_temp[i])):
        safe_reports_temp[i][j] = int(safe_reports_temp[i][j])


for i in range(len(safe_reports_temp)):
    for j in range((len(safe_reports_temp[i]))):
        if 
