import re

file_path = r'C:\Users\toleg\OneDrive\Рабочий стол\PP2_Sum_Aibek\Lab_Works_Summer\row.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

pattern = 'ab*'

matches = re.findall(pattern, data)
for match in matches:
    print(match)