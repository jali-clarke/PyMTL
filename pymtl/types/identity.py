from pymtl import Applicative

class Identity(Applicative):
    
    def __init__(self, a):
        self.value = a

    @classmethod
    def pure(cls, a):
        return cls(a)

    def ap(self, fa):
        return Identity(self.value(fa.value))
