import re

def match_lowercase_letters():
    file_path = r'C:\Users\toleg\OneDrive\Рабочий стол\PP2_Sum_aibek\Lab_Works_Summer\Lab_5\row.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(data)
    return matches

print("Task:", match_lowercase_letters())