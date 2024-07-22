from typing import Generator

def fib(n: int) -> Generator[int, None, None]:
    yield 0 # special case
    if n > 0: yield 1 # special case
    last: int = 0 # initialy defined for fib(0)
    next: int = 1 # initialy defined for fib(1)
    for _ in range(1,n):
        last, next = next, last+next
        yield next # main case for generator

if __name__=="__main__":
    for i in fib(50):
        print(i)