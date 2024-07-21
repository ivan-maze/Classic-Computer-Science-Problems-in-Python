def fib(n: int) -> int:
   if n <2: # caso de base
    return n
   return fib(n-1) + fib(n-2) # caso recursivo

if __name__=="__main__":
    print(fib(5))
    print(fib(10))