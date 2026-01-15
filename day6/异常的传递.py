
def demo1():
    return int(input("输入整数:"))

def demo2():
    num=demo1()
    return num

# try:
#     print(demo2())
# except Exception as e:
#     print("错误%s"%e)
print(demo2())