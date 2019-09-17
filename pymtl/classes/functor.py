import abc

class Functor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fmap(self, f):
        pass