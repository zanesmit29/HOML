from pathlib import Path
import os

print(Path.cwd())  # This will print the current working directory
print(os.getcwd())  # This will also print the current working directory
print(Path.home())  # This will print the home directory of the user

p = Path.cwd()
print(p.parts)  # This will print the parts of the path as a tuple
print(p.parts[2])  # This will print the third part of the path

for name in Path.cwd().glob('*'):
    print(name)  # This will print all files and directories in the current working directory

win_dir = Path('C:/Windows')
print(win_dir.exists())  # This will check if the path exists
print(win_dir.is_dir())  # This will check if the path is a directory
print(win_dir.is_file())  # This will check if the path is a file

# p = Path('spam.txt')
# p.write_text('Hello, world!')  # This will write 'Hello, world!' to the file spam.txt
# print(p.read_text())  # This will read the content of the file spam.txt
# p.rename('eggs.txt')  # This will rename the file spam.txt to eggs.txt
# p.unlink()  # This will delete the file eggs.txt

# egg_file = open(Path.cwd() / 'eggs.txt', 'w', encoding='UTF-8') 
# eggs_content = egg_file.write('Hello, world!')  # This will write 'Hello, world!' to the file eggs.txt
# egg_file.close()
# egg_file = open('eggs.txt', encoding='UTF-8')
# content = egg_file.read()
# print(content)

# with open('eggs.txt', 'w', encoding='UTF-8') as file_obj:
#     file_obj.write('Hello, world!')
# with open('eggs.txt', encoding='UTF-8') as file_obj:
#     content = file_obj.read()
#     print(content)

