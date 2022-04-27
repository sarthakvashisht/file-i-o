import os
def open_files( **kwargs):
    size = []
    num = int(no_of_line)
    arc = kwargs.get('file')
    if os.path.isfile(arc):
        arc_f = open(arc, 'r')
        lines = arc_f.readlines()
        for line in lines:
            size.append(line)
    if num > len(size) or num < 1:
        print("Enter valid number")
    else:
        print(size[num:num+1])
p = input("what is the path to the file")
while True:
    no_of_line = input("line number")
    if no_of_line != 'q':
        no_of_line = int(no_of_line)
        open_files(file=p, x=no_of_line)
    else:
        print("thanks & bye")
        break
