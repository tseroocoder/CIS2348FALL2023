# Michelle Oteri
# 2252197
lines = []
file = open(r"C:inputDates.txt", "r")

# loop through each line in the file
for line in file:
# strip the newline character from the line
line = line.strip()
# append the line to the list
lines.append(line)

# close the file
print(lines)
file.close()
    