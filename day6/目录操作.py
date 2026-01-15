import os

def use_rename():
    # os.rename('file3.txt','file4')
    # os.rename('D:\\PyCharm1\\day6\\file4','D:\\PyCharm1\\day6\\file3')
    # os.rename('dir1\\file1','dir1\\file2')#需要转义
    os.rename('dir1/file2','dir1/file1')#相对路径

def use_dir_func():
    file_list=os.listdir('.')
    print(file_list)
    # os.rmdir('dir2')
    # os.mkdir('dir2')
    print(os.getcwd())
    os.chdir('dir2')
    file=open('file1','w',encoding='utf8')
    file.close()

def scan_dir1(current_path, width):
    """深度优先遍历
    :param current_path:
    :return:
    """
    file_list = os.listdir(current_path)  # 得到当前文件夹下的所有文件
    for file in file_list:
        print(' ' * width, file)  # 打印文件名,width代表多少个空格
        if os.path.isdir(file):
            scan_dir1(file, width + 4)

def scan_dir2(current_path, width):
    """深度优先遍历
    :param current_path:
    :return:
    """
    file_list = os.listdir(current_path)  # 得到当前文件夹下的所有文件
    for file in file_list:
        print(' ' * width, file)  # 打印文件名,width代表多少个空格
        new_path=current_path+'/'+file #把当前路径和文件名拼接到一起
        if os.path.isdir(new_path):
            scan_dir2(new_path, width + 4)
def use_stat(file_path):
    #获取文件大小
    file_info = os.stat(file_path)
    print('size{},uid{},mode:{:x},mtime{}'.format( file_info.st_size, file_info.st_uid,
    file_info.st_mode, file_info.st_mtime))
    from time import strftime
    from time import gmtime
    gm_time=gmtime(file_info.st_mtime)
    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime(file_info.st_mtime)))

if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # scan_dir2('D:\\PyCharm1\\day6',0 ) #绝对路径
    # scan_dir2('.',0 ) #相对路径
    use_stat('file1')