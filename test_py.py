import example

def test_read_file():
    assert type(example.read_file()) == list
    

def test_create_canvas():
    class F():
        def write(*args):
            pass
    coord = ['C','20','4']
    f = F()
    assert example.create_canvas(coord,f) == True
    

def test_create_line_vertical():
    class F():
        def write(*args):
           pass
        def seek(*args):
            pass
    coord = ['','6','3','6','4']
    f = F()
    w = '20'
    assert example.create_line(coord,f,w) == 'vertical'

def test_create_line_horizontal():
    class F():
        def write(*args):
           pass
        def seek(*args):
            pass
    coord = ['','1','2','6','2']
    f = F()
    w = '20'
    assert example.create_line(coord,f,w) == 'horizontal'


def test_create_rectangle():
    class F():
        def write(*args):
           pass
        def seek(*args):
            pass
    coord = ['','16','1','20','3']
    f = F()
    w = '20'
    assert example.create_rectangle(coord,f,w) == True


def test_backet_fill():
    class F():
        def write(*args):
           pass
        def read(*args):
            pass
        def seek(*args):
            pass
    coord = ['','10','3','o']
    f = F()
    w = '20'
    assert example.backet_fill(coord,f,w) == True
    
def test_write_file():
    coord = [['C', '20', '4'],
             ['L', '1', '2', '6', '2'],
             ['L', '6', '3', '6', '4'],
             ['R', '16', '1', '20', '3'],
             ['B', '10', '3', 'o']
             ]
    
    assert example.write_file(coord) == True
