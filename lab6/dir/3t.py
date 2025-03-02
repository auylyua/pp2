import os
def items(path):
    if os.path.exists(path):
        print("exists!")

    file = os.path.basename(path)
    print("file's name: ", file)
    directory = os.path.dirname(path)
    print("folder's name: ", directory)

path = input("enter the path: ")
items(path)