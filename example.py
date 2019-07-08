def read_file():
    #reading file input.txt and append lines in list

    lines=[]
    with open('input.txt','r') as f:
        for line in f:
            lines.append(line.split())
    print(lines)
    return lines


def create_canvas(coord,f):
    #canvas is created
    
    f.write('-'+int(coord[1])*'-'+'-')
    f.write('\n')
    for i in range(int(coord[2])):
        f.write('|'+int(coord[1])*' '+'|')
        f.write('\n')
    f.write('-'+int(coord[1])*'-'+'-')
    return True

def create_line(coord,f,w):
    #line is created
    
    if coord[1] == coord[3]:            #vertical line check
        length = int(coord[4])-int(coord[2])+1
        xy = int(coord[2])*(int(w)+4)+int(coord[1])
        f.seek(xy)
        for i in range(length):
            f.write('X')
            xy+=int(w)+4
            f.seek(xy)
        return 'vertical'
    elif coord[2] == coord[4]:              #horizontal line check
        length = int(coord[3])-int(coord[1])+1
        xy = int(coord[2])*(int(w)+4)+int(coord[1])
        f.seek(xy)
        f.write(length*'X')
        return 'horizontal'

    
def create_rectangle(coord,f,w):
    #rectangle is created
    
    length = int(coord[3])-int(coord[1])+1
    height = int(coord[4])-int(coord[2])
    xy = int(coord[2])*(int(w)+4)+int(coord[1])
    f.seek(xy)
    f.write(length*'X')
    f.seek(xy)
    for i in range(height):
            xy+=int(w)+4
            f.seek(xy)
            f.write('X'+(length-2)*' '+'X')
            
    xy = int(coord[4])*(int(w)+4)+int(coord[1])
    f.seek(xy)
    f.write(length*'X')
    return True
    
def backet_fill(coord,f,w):
        def recursion(xy,char,w):
            f.seek(xy)
            str = f.read(1)
            if str == ' ' :
                f.seek(xy)
                f.write(char)
                recursion(xy+int(w)+4,char,w)
                recursion(xy-int(w)-4,char,w)
                recursion(xy-1,char,w)
                recursion(xy+1,char,w)
        xy = int(coord[2])*(int(w)+4)+int(coord[1])
        recursion(xy,coord[3],w)
        return True

def write_file(coordinates):
    with open('output.txt','w+') as f:
        create_canvas(coordinates[0],f)
        for i in coordinates:
            if i[0] == 'L':
                create_line(i,f,coordinates[0][1])
            if i[0] == 'R':
                create_rectangle(i,f,coordinates[0][1])
            if i[0] == 'B':
                backet_fill(i,f,coordinates[0][1])
    return True

def main():
    lines = read_file()
    if lines[0][0] == 'C':          #check canvas 
        write_file(lines)


if __name__ == "__main__":
    main()
