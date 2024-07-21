from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int: # same code in the second task, using just base cases
    if n <2: # base cases
        return n
    return fib(n-1) + fib(n-2) # recursive case
       
if __name__=="__main__":
    print(fib(5))
    print(fib(500))