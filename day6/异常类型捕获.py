import traceback
import sys

def use_exception1():
      try:
          num=int(input("输入一个整数："))
          result=4/num
          print(result)
      except:
          print("你输入的不是整数")


def use_exception2():
    while True:
        try:
            num = int(input("输入一个整数："))
            result = 4 / num
            print(result)
            break
        except:
            print("你输入的不是整数")


def use_exception3():
    try:
        num = int(input("输入一个整数："))
        result = 4 / num
        print(result)
    except ValueError:#类型判断
        print("你输入的不是整数")
    except ZeroDivisionError:#除0错误
        print("整除0错误")


def use_exception4():
    try:
        num = int(input("输入一个整数："))
        result = 4//num#//整型结果，/浮点型结果
        print(result)
    except ValueError:
        print("你输入的不是整数")
    except Exception as e:#捕获未知错误,e为异常别名
        print(e)

def use_exception5():
    try:
        num = int(input("输入一个整数："))
        result = 4//num#//整型结果，/浮点型结果
        print(result)
        return
    except ValueError:
        print("你输入的不是整数")
        return
    except ZeroDivisionError:#除0错误
        print("整除0错误")
    except Exception as e:#捕获未知错误,e为异常别名
        print(e)
    else:
        print("正常执行完成")
    finally:#不论执行是否正确，以及是否前面提前return，依然会执行该语句
        print("执行完成，但不保证正确")


def use_exception6():
    try:
        num = int(input("输入一个整数："))
        result = 4//num#//整型结果，/浮点型结果
        print(result)
    except Exception as e:#捕获未知错误,e为异常别名
        print(e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        file_name = exc_traceback.tb_frame.f_code.co_filename  # 异常发生的文件 全称
        line_num = exc_traceback.tb_lineno  # 异常发生的 精确行号
        error_msg = str(e)  # 异常的具体描述信息
        print(f"异常发生文件：{file_name}")
        print(f"异常发生行号：{line_num}")

if __name__ == '__main__':
    # use_exception1()
    # use_exception2()
    use_exception6()