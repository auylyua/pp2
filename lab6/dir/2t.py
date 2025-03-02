import os 
def access(path):
    if os.path.exists(path):
        print("exists!")
    if os.access(path, os.R_OK):
        print("Readable")
    if os.access(path, os.W_OK):
        print("Writable")
    if os.access(path, os.EX_OK):
        print("Executable")
path = input("Введите путь: ")
access(path)