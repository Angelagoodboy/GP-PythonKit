from  tkinter import *
import tkinter
import OpenFile
from OpenFile import *
from  tkinter  import ttk

class  MainActivity(object):
    global path

    def _init_(self):
        print('执行初始化方法')
    def callback(self):
        openFile(self)
    def Main(self):
        global path
        path=tkinter.StringVar
        root = tkinter.Tk()  # 生成root主窗口
        root.title('软件bin upgrade')
        root.resizable(0, 0)
        root.geometry('500x330')
        menu = tkinter.Menu(root)
        root['menu'] = menu
        # menumenu.add_command(label='菜单')
        menu.add_cascade(label='打开文件', command=self.callback)
        menu.bind('<Button-1>',open)
        label_carType = tkinter.Label(text="选择车型", font=('Arial', 10)).place(x=60, y=40, width=100, height=30)
        comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist = ttk.Combobox(root, textvariable=comvalue)  # 初始化
        comboxlist["values"] = ("奥迪", "奔驰", "宝马", "雷克萨斯")
        comboxlist.current(0)  # 选择第一个
        comboxlist.bind("<<ComboboxSelected>>", root)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
        comboxlist.place(x=160, y=40, width=100, height=30)
        label_path = tkinter.Label(text="输出路径", font=('Arial', 10)).place(x=60, y=80, width=100, height=30)
        Entry_path = tkinter.Entry(root,textvariable=path).place(x=160,y=80,width=250,height=25)
        btn_browse = tkinter.Button(root, text='浏览').place(x=420, y=80, width=80, height=25)
        btn_confirm=tkinter.Button(root,text='确认写入').place(x=150,y= 120,width=80,height=25)
        root.mainloop()  # 进入消息循环（必需组件）

if __name__ == '__main__':
      MainActivity().Main()
