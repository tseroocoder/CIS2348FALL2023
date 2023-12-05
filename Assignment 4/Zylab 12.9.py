# Michelle Oteri
#2252197
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        # FIXME: The following line will throw ValueError exception.
        #        Insert try/except blocks to catch the exception.
        age = int(parts[1]) + 1
    except ValueError:
        age = 0

    print(f'{name} {age}')


    parts = input().split()
    name = parts[0]
