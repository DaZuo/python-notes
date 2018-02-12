"""Modules"""

def fib(arg_n):
    """Test"""
    val_a, val_b = 0, 1
    while val_b < arg_n:
        print(val_b, end=" ")
        val_a, val_b = val_b, val_a+val_b
    print()

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    print(sys.path)
