with open("fileopen.py", "r") as file:
    lines = file.readlines()
    specific_line = lines[2]
    print(specific_line)