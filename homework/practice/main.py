#1
file1 = open('file.txt', 'r')
print(file1.read())
file1.close()
#2
file2 = open('file2.txt', 'w')
for i in range(1,11):
    file2.write(str(i) + "\n")
file2.close()
file2 = open('file2.txt', 'r')
print(file2.read())
file2.close()
#3
file3 = open('file3.txt', 'w')
names = ['aigerim', 'dana', 'arsen', 'aliya']
for name in names:
    file3.write( name + "\n")
file3.close()
with open('file3.txt', 'r') as f:
    for line in f:
        print(line.strip().capitalize())