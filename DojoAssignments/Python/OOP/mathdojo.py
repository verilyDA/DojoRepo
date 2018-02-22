class math(object):
    def __init__(self):
        self.mathsum = 0
    def add(self, *varg):
        for x in range(0, len(varg)):
            if type(varg[x]) is list:
                for each in varg[x]:
                    self.mathsum += each
                continue
            if type(varg[x]) is tuple or type(varg[x]) is tuple:
                for vars in varg[x]:
                    self.mathsum += vars
                continue
            self.mathsum += varg[x]
        return self
    def subtract(self, *varg):
        for x in range(0, len(varg)):
            if type(varg[x]) is list or type(varg[x]) is tuple:
                for each in varg[x]:
                    self.mathsum -= each
                continue
            self.mathsum -= varg[x]
        return self
    def display(self):
        print (self.mathsum)
        self.mathsum = 0
        return self


m1 = math()
m1.add(2).add(2,5).subtract(3,2).display()
m1.add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).display()
