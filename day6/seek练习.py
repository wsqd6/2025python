import os

def seek_start():
    """
    相对于（文件起始位置）开头偏移
    :return: 
    """
    file=open('file1',mode='r+',encoding='utf8')
    file.seek(8,os.SEEK_SET)#任意汉字的偏移量是3的整数倍
    text = file.read(8)
    print(text)
    file.close()
def seek_end():
    """
    相对于（文件尾部）末尾偏移
    :return:
    """
    file=open('file1',mode='r+',encoding='utf8')
    file.seek(0,os.SEEK_END)#只能是0,读不到内容
    text = file.read(5)
    print(text)
    file.close()
def seek_cur():
    """
    相对于当前位置偏移
    :return:
    """
    file=open('file1',mode='r+',encoding='utf8')
    file.seek(0,os.SEEK_CUR)
    text = file.read(6)
    print(text)
    file.close()

def seek_b_cur():
    """
    相对于当前位置偏移
    在b模式下，读到的是字节流,读取图片，音频，视频
    :return:
    """
    file=open('file1',mode='rb+')
    # file1.seek(5,os.SEEK_CUR)
    # file1.seek(-2,os.SEEK_CUR)
    file.seek(-3,os.SEEK_END)
    b=file.read()
    print(b)
    file.close()

def copy_file():
    file1=open('img.png',mode='rb+')
    file2=open('img_copy.png',mode='wb')
    b=file1.read()
    file2.write(b)
    file1.close()
    file2.close()

def modify_movie():
    file1=open('img.png',mode='rb+')
    file1.seek(10,os.SEEK_SET)
    b=file1.read(1)
    print(b)
    new_b = bytes([~ord(b) & 0xFF])
    file1.seek(10, os.SEEK_SET)
    file1.write(new_b)
    print("取反字节",new_b)
    file1.close()
if __name__=='__main__':
    # seek_start()
    #seek_end()
    # seek_cur()
    # seek_b_cur()
    # copy_file()
    modify_movie()