import  os
from tkinter import filedialog
global file_path
global file_text

def openbinFile():

    '打开文件'

    file_path = filedialog.askopenfilename(title='选择文件',initialdir=(os.path.expanduser('C:/')))
    print('打开文件：', file_path)
    return file_path



def writeFile(file_path,data):
    '写入文件'
    tmp=bytes(1024)
    if file_path is not None:
        with open(file_path, mode='rb') as file:
            #读出原来的内容
            while True:
                strb = file.read(1024)
                if strb == b"":
                    break
                print(strb)
                tmp=strb
        file.write(data)
        file.append(tmp)
