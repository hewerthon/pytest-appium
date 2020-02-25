file = open('test.txt')
# Read all the contents of file
#print(file.read())
# Read n number of characters by passing parameter
#print(file.read(2))

# read one sing line at a time realine()
# print(file.readline())
# print(file.readline())

for i in file.readlines():
    print(i)
file.close()

# print line by line using readline method


