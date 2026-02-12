#1
with open('file.csv', 'r') as f:
    print(f.read())
#2
with open('file2.csv', 'w') as f2:
    for i in range(1, 11):
        f2.write(str(i) + '\n')
with open('file2.csv', 'r') as f2:
    print(f2.read())
#3
names = ['aigerim', 'dana', 'arsen', 'aliya']
with open('file3.csv', 'w') as f3:
    for name in names:
        f3.write(name.capitalize() + '\n')
with open('file3.csv', 'r') as f3:
    print(f3.read())