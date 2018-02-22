class call(object):
    uid = 0
    def __init__(self, name, phoneNum, time, reason):
        call.uid += 1
        self.id = call.uid
        self.name = name
        self.phoneNum = phoneNum
        self.time = time
        self.reason = reason
    def display(self):
        print('ID: ', self.id)
        print('Name: ', self.name)
        print('Phone Number: ', self.phoneNum)
        print('Time: ', self.time)
        print('Reason: ', self.reason)
        return self
class callCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)
    def add(self, call):
        self.calls.append(call)
        self.queue = len(self.calls)
        return self
    def drop(self):
        self.calls.pop(0)
        self.queue = len(self.calls)
        return self
    def info(self):
        print('Queue length', self.queue)
        for x in self.calls:
            print('Name: ', x.name, ' Number: ', x.phoneNum)

c1 = call('Dan the first', '555-0123', 'now', 'sayin hi')
c1.display()
c2 = call('Dan the second', '555-0123', 'now', 'not sayin hi')
c2.display()

ccenter = callCenter()
ccenter.add(c1).add(c2).info()
ccenter.drop().info()
