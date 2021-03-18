import fibo as mod
import sys

# mod.fib(10)
# mod.fib(int(sys.argv[1]))

if __name__ == "__main__":
    mod.fib(int(sys.argv[1]))