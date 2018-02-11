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

test_if_statements()
