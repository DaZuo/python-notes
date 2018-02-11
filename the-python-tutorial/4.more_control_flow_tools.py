"""More Control Flow Tools"""

def test_if_statements():
    """测试 if 语句"""
    val_x = int(input("Please enter an integer: "))
    if val_x < 0:
        val_x = 0
        print("Negative changed to zero")
    elif val_x == 0:
        print("Zero")
    elif val_x == 1:
        print("Single")
    else:
        print("More")

# test_if_statements()

def test_for_statements():
    """测试 for 语句"""
    words = ["cat", "window", "defenestrate"]
    for var_w in words:
        print(var_w, len(var_w))

# test_for_statements()

def test_range_function():
    """测试 range 函数"""
    for var_i in range(5):
        print(var_i)

# test_range_function()

def test_loop_statements():
    """测试循环语句"""
    for var_n in range(2, 10):
        for var_x in range(2, var_n):
            if var_n % var_x == 0:
                print(var_n, "equals", var_x, "*", var_n//var_x)
            else:
                break
        else:
            # loop fell through without finding a factor
            print(var_n, "is a prime number")

# test_loop_statements()

# def test_function_annotations(ham: str, eggs: str = "eggs") -> str:
#     """测试函数"""
#     print("Annotations:", test_function_annotations.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + " and " + eggs

# test_function_annotations("spam")

def test_function_annotations(ham, eggs):
    """测试函数"""
    print("Annotations:", test_function_annotations.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs

test_function_annotations("spam", "eggs")
