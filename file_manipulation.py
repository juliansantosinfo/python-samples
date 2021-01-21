# Function open https://docs.python.org/3.8/library/functions.html#open

# open to read.
with open('file_manipulation.py', 'r') as file:

    # read one next line.
    line = file.readline()
    print(line, end='')

    # Go to start file.
    file.seek(0, 0)

    # read all lines with for.
    for line in file.readlines():
        print(line, end='')

    # Go to start file.
    file.seek(0, 0)

    # Get line files in list.
    listLines = file.readlines()
    for line in listLines:
        print(line, end='')


# open to write.
with open('write.txt', 'w+') as file:

    # Write in file.
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')

    # Go top.
    file.seek(0 ,0)

    # print result.
    for line in file.readlines():
        print(line, end='')

    # Write in file list.
    listLines = ['Line 4\n', 'Line 5\n', 'Line 6\n']
    file.writelines(listLines)

    # Go top.
    file.seek(0 ,0)

    # print result.
    for line in file.readlines():
        print(line, end='')


# open to append.
with open('append.txt', 'a+') as file:

    # Write in file list.
    listLines = ['Line\n', 'Line\n', 'Line\n']
    file.writelines(listLines)

    # Go top.
    file.seek(0 ,0)

    # print result.
    for line in file.readlines():
        print(line, end='')

