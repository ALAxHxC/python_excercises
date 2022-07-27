class Computer():
    def __init__(self, computer='XXX', ram='', storage=''):
        self.computer = computer
        self.ram = ram
        self.storage = storage

# Class Mobile inherits Computer
class Mobile(Computer):
    def __init__(self):
        super().__init__('xxxx','64','2tb')

mobile = Mobile()
print(mobile.ram,mobile.computer,mobile.storage)