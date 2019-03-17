class Testing:
    def __init__(self):
        self.name = 'Josh'
        self.age = 21
josh = Testing()

def access(object):
    josh.age += 10
    if josh.age != 21:
        print('Works')

access(josh)
print(josh.age)