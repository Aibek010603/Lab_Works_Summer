import re

def match_a_to_b(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    pattern = re.compile(r'a.*b')
    matches = pattern.findall(data)
    return matches

# Заменяем ваш путь к файлу на указанный вами
file_path = r'C:\Users\toleg\OneDrive\Рабочий стол\PP2_Sum_aibek\Lab_Works_Summer\Lab_5\row.txt'

print("Task:", match_a_to_b(file_path))
