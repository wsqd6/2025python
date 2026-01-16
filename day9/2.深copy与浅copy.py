import copy
def use_list_copy():
    """
    使用列表自身的copy
    :return:
    """
    a = [1, 2, 3]
    b = a.copy()
    c = a
    b[0] = 10
    print(id(a))
    print(id(b))
    print(id(c))
    print(a)
    print(b)
    print(c)
def use_copy():
    """
    使用copy包中自带的copy
    :return:
    """
    a=[1,2,3]
    b=copy.copy(a)  #可放可变数据类型
    b[0]=10
    c=a
    print(id(a))
    print(id(b))
    print(id(c))
    print(a)
    print(b)
    print(c)

def use_copy2():
    """
    copy是浅copy,只做第一层的copy
    :return:
    """
    a=[1,2]
    b=[3,4]
    c=[a,b]
    d=copy.copy(c)
    print(id(c))
    print(id(d))
    a[0]=10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-'*50)
    #只copy一次，若可变数据类型里还有可变数据类型元素，则里面的元素不再改变，适用于可变数据类型的元素为不可变数据类型
    print(id(c[0]),id(c[1]))
    print(id(d[0]),id(d[1]))

def use_deepcopy():
    """
    深copy，不管多少层，都会新做一个空间，把数据拿进来
    :return:
    """
    a=[1,2]
    b=[3,4]
    c=[a,b]
    d=copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0]=10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0]),id(c[1]))
    print(id(d[0]),id(d[1]))

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.item=['衣服','帽子']

def use_copy_own_obj():
    """
    实际对自定义对象的练习
    :return:
    """
    old_s1=Student('dw',20)
    # new_s1=copy.copy(old_s1)
    new_s1=copy.deepcopy(old_s1)
    new_s1.age=22   #deepcopy 新对象修改后，原对象不会受到影响
    new_s1.item.append('裤子')
    print(old_s1.age)
    print(old_s1.item)

if __name__ == '__main__':
    # use_copy()
    # use_list_copy()
    # use_copy2()
    # use_deepcopy()
    use_copy_own_obj()