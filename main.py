# This is a sample Python script.
import sys
sys.setrecursionlimit(10**7)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

count = 0

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def fib(n):
    global count
    count += 1
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    fib=memoize(fib)
    print(fib(996))
    length = 0
    n=fib(996)
    while n > 0:
        n //= 10
        length += 1
    print(length)
