from sys import argv

script, filename = argv

txt = open(filename, encoding="ISO-8859-1")

print(f"Содержимое файла {filename}:")
print(txt.read())

print("Снова введите имя файла:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())