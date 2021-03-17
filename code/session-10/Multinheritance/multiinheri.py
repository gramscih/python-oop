class A(object):
    def __init__(self, name):
        self.name = name

class B(object):
    def __init__(self, b_id):
        self.id = b_id


class C(B, A):
    def __init__(self, name, id):
        A.__init__(self, name)
        B.__init__(self, b_id = id)


ob = C("Gramsci", 123)
print(ob.name)
print(ob.id)
