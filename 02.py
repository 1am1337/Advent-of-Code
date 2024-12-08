import re
complete_file = None
safe_reports = []
safe_reports_temp = []
increase_list = []
with open("02.txt") as file:
    complete_file = file.read()
safe_reports_temp = complete_file.split("\n")
for i in range(len(safe_reports_temp)):
    safe_reports_temp[i] = safe_reports_temp[i].split(" ")

for i in range(len(safe_reports_temp)):
    for j in range(len(safe_reports_temp[i])):
        safe_reports_temp[i][j] = int(safe_reports_temp[i][j])

for i in range(len(safe_reports_temp)):
    increase_list = []
    if safe_reports_temp[i] == sorted(safe_reports_temp[i]) or safe_reports_temp[i] == sorted(safe_reports_temp[i], reverse = True):
        safe_reports_temp[i] = sorted(safe_reports_temp[i])
        for j in range((len(safe_reports_temp[i])-1)):
            if safe_reports_temp[i][j+1] - safe_reports_temp[i][j] < 4 and safe_reports_temp[i][j+1] - safe_reports_temp[i][j] > 0:
                increase_list.append(True)
            else:
                increase_list.append(False)
        if False in increase_list:
            continue
        else:
            safe_reports.append(safe_reports_temp[i])


    
print(safe_reports)
print(len(safe_reports))
