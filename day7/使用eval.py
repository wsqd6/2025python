import os


def read_conf():
    """
    读取配置
    :return:
    """
    file=open('file1','r+',encoding='utf8')
    text_info=file.read()
    print(text_info)
    my_dict=print(eval(text_info))
    print(type(my_dict))
    file.close()

if __name__ == '__main__':
    # read_conf()
    # os.system('rd /s /q dir2')  #windows删除目录
    eval("__import__('os').system('dir')") #不要用eval执行前端发过来的任何子串