def open_r():
    file=open('file2.txt',mode='r',encoding='utf-8')
    text=file.read()
    print(text)
    file.close()
def open_wr():
    file=open('file1',mode='r+',encoding='utf-8')
    text=file.read()
    print(text)
    file.write('world')
    file.close()
def open_w():
    file=open('file3.txt',mode='w',encoding='utf-8')#w只写，可以创建新文件，或者若存在则覆盖前一文件，r，r+不可以
    #file1.write('今天开始')
    file.close()
def open_a():
    file=open('file1',mode='a',encoding='utf-8')#追加到文件末尾
    file.write('今天开始')
    file.close()
if __name__=='__main__':
    #open_r()
    open_r()
    #open_a()