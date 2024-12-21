def custom_write(file_name: str, strings: str):
    strings_positions = {}
    file_1 = open(file_name, 'w', encoding='utf-8')
    line_number = 1
    for i in strings:
        line_byte = file_1.tell()
        file_1.write(i + '\n')
        strings_positions[(line_number, line_byte)] = i
        line_number += 1
    file_1.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]



result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)