import re

def match_two_to_three_b():
    file_path = r'C:\Users\toleg\OneDrive\Рабочий стол\PP2_Sum_aibek\Lab_Works_Summer\Lab_5\row.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    pattern = re.compile(r'ab{2,3}')
    matches = pattern.findall(data)
    return matches

print("Task 2:", match_two_to_three_b())