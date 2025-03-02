import string  
def letters(): 
    for letter in string.ascii_uppercase: 
        filename = f"{letter}.txt" 
        with open(filename, "w") as file: 
            file.write(f"File {filename}\n") 
    print("file A.txt to Z.txt is ready")  
letters()