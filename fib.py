#!/usr/bin/env python3

fibSeq = [0,1] 
  
def fib(n): 
    if n < 0: 
        print("Can't have -ve fibonacci") 
    elif n <= len(fibSeq):
        return fibSeq[n-1]
    else:
        temp = fib(n-1) + fib(n-2) 
        fibSeq.append(temp)
        return temp
  
print(f"9th Fibonacci number is: {fib(9)}")
