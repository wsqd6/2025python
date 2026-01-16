
#把文件夹添加到搜索路径，或者用其他方法，例如直接使用包，导包即可
import sys

# sys.path.append('module')
sys.path.insert(0,'module')
print(sys.path)
print('-'*50)

import my_module  #pycharm的问题

my_module.test1()