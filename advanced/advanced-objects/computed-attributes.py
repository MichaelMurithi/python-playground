# customize string representations of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red,self.green,self.blue) 
        elif attr == 'hexcolor':
            return f'{self.red:02x}{self.green:02x}{self.blue:02x}'
        return 'Attribute error'
    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
                 
        super().__setattr__(attr, val)

    # TODO: use dir to list the available properties
    def __dir__(self):
        return ["red", 'green', 'blue', 'rgbcolor', 'hexcolor']

def main():
    # create an instance of myColor
    color1 = myColor()
    # TODO: print the value of a computed attribute
    print(color1.rgbcolor)
    print(color1.hexcolor)
    print(color1.hexcol)
    
    # TODO: set the value of a computed attribute
    color1.rgbcolor = (250,10,16)
    print(color1.rgbcolor)
    print(color1.hexcolor)
    # TODO: access a regular attribute
    print(color1.red)
    # TODO: list the available attributes
    print(dir(color1))

if __name__ == "__main__":
    main()
