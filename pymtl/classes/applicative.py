import abc

from .functor import Functor

class Applicative(Functor):

    @classmethod
    @abc.abstractmethod
    def pure(cls, a):
        pass

    @abc.abstractmethod
    def ap(self, fa):
        pass

    def fmap(self, f):
        return self.pure(f).ap(self)