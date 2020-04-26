from  tkinter import *
import tkinter,UI_Event
import OpenFile
from OpenFile import *
from  tkinter  import ttk

class  MainActivity(object):
    helloCommboxEvent=UI_Event.helloCommboxEvent

    def _init_(self):
        print('执行初始化方法')
    def callback(self):
        openbinFile(self)
    def callback_combobox(self,value):
        self.helloCommboxEvent.comboxselectEvent( self.helloCommboxEvent,value)
    def callback_brwser(self):
        self.helloCommboxEvent.btn_browse(self.helloCommboxEvent)
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

        label_carType = tkinter.Label(text="选择车型", font=('Arial', 10)).place(x=60, y=40, width=100, height=30)
        comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist = ttk.Combobox(root, textvariable=comvalue)  # 初始化
        comboxlist["values"] = ("宝马STM32F105RBT6", "宝马8823", "8368奥迪高配", "8368奥迪低配","8368奥迪Q7换屏","8368雷克萨斯","8368宝马NBT","8368宝马CIC","8368奔驰1"
                                                                                                                                     "8368奔驰2")
        comboxlist.current(0)  # 选择第一个
        comboxlist.bind("<<ComboboxSelected>>", lambda event :self.callback_combobox(comboxlist.get()))
        comboxlist.place(x=160, y=40, width=100, height=30)
        label_path = tkinter.Label(text="输出路径", font=('Arial', 10)).place(x=60, y=80, width=100, height=30)
        default_value = StringVar()
        default_value.set('1')
        Entry_path = tkinter.Entry(root,textvariable=default_value).place(x=160,y=80,width=250,height=25)
        btn_browse = tkinter.Button(root, text='浏览',command=self.callback_brwser).place(x=420, y=80, width=80, height=25)

        btn_confirm=tkinter.Button(root,text='确认写入').place(x=150,y= 120,width=80,height=25)
        root.mainloop()  # 进入消息循环（必需组件）

if __name__ == '__main__':
      MainActivity().Main()
