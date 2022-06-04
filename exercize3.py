import os

BASE_PATH = os.getcwd()

def file_basename(file_name):
    return os.path.basename(os.path.join(BASE_PATH, file_name))

def len_doc(file_name):
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        lines = file_obj.readlines()
        return len(lines)

def data_files(file_name):
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        a = file_obj.read()
        return a




with open('3.txt', 'a', encoding='utf-8') as file_obj:
    if len_doc('1.txt') < len_doc('2.txt'):
        file_obj.write(f'{file_basename("1.txt")}\n{str(len_doc("1.txt"))}\n{data_files("1.txt")}\n')
        file_obj.write(f'{file_basename("2.txt")}\n{str(len_doc("2.txt"))}\n{data_files("2.txt")}\n')
    else:
        file_obj.write(f'{file_basename("2.txt")}\n{str(len_doc("2.txt"))}\n{data_files("2.txt")}\n')
        file_obj.write(f'{file_basename("1.txt")}\n{str(len_doc("1.txt"))}\n{data_files("1.txt")}\n')

print(data_files('1.txt'))

