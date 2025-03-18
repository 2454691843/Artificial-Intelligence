import window as win
'''Please enter this code into the terminal:
    pip install requests
'''
class Main:
    def runApp(self):
        # 创建应用实例
        self.app = win.ChatApp()
        self.app.chat_area.tag_configure('right', justify='right')
        self.app.chat_area.tag_configure('left', justify='left')
        # 启动主循环
        self.app.root.mainloop()

if __name__ == "__main__":
    main = Main()
    main.runApp()
