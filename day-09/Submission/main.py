
with open("story.txt", "r") as file:
    lines = file.readlines()

    counter = len(lines)

    print("Number of lines: ", counter) 