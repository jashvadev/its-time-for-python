with open("fileopen.py", "r") as file:
    lines = file.readlines()
    specific_line = lines[3]
    print(specific_line.strip())