#Michelle Oteri
#2252197
import csv

file = open(input())

strings = csv.reader(file, delimiter=',')

words = []

for row in strings:

    for word in row:
        words.append(word.strip())

for i in range(len(words)):

    if words[i] not in words[:i]:

        count = 0

        for j in range(len(words)):

            if words[i] == words[j]:
                count += 1

        print(words[i], count)

file.close()