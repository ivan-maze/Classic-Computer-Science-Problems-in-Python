def fib(n: int) -> int:
    return fib(n-1) + fib(n-2)

if __name__=="__main__":
    print(fib(5))