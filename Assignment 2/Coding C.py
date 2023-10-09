# Michelle Oteri
# 2252197
lines = []
file = open(r"C: Homework.txt", "r")


for line in file:
 line = line.strip()
 lines.append(line)

file.close()

file_new = open("parseDates.txt", "w")

for date in lines[:-1]:
   print(date)
   output_date = date_format_new(date)
   print(output_date)
   if output_date == 'None':
       pass
   else:
       file_new.write(output_date + "\n")
    