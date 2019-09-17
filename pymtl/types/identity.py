from typing import TypeVar, Generic, Callable
from pymtl import Functor

A = TypeVar('A')
B = TypeVar('B')

class Identity(Functor, Generic[A]):
    
    def __init__(self, a: A) -> None:
        self._a: A = a

    def fmap(self, f: Callable[[A], B]) -> Identity[B]:
        return Identity(f(self._a))