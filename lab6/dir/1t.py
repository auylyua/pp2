import os
def list(path):
    try:
        items = os.listdir(path)
        only_dir = [item for item in items if os.path.isdir(os.path.join(path,item))]
        only_file = [item for item in items if os.path.isfile(os.path.join(path,item))]
        print("Folders")
        print(only_dir)
        print("\n Files")
        print(only_file)
        print("\n All ")
        print(items)
    except FileNotFoundError:
        print("Error, there are no such file")
    except PermissionError:
        print("Error, you dont have a permission to file")
path = input("Enter a path to file: ")
list(path)