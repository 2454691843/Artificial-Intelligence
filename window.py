import tkinter as tk
from tkinter import ttk, scrolledtext
from api import get_response

def ai_response(user_input: str) -> str:
    return user_input

class ChatApp:
    def __init__(self):
        self.root = tk.Tk()
        self.size = self.root.maxsize()
        self.width,self.height = self.size
        self.width,self.height = self.width - 100,self.height - 100
        self.root.title('Chat window')
        self.root.geometry(f'{self.width}x{self.height}+50+65')
        self.root.attributes('-alpha',0.9)
        self.root.configure(bg = 'lightgray')
        self.create_widgets()
    def create_widgets(self) -> None:
        """创建并布局所有 GUI 组件
        
        包含聊天区域、输入框、发送按钮的创建和布局配置
        """
        # 聊天记录区域（带滚动条）
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            width=self.width-100,
            height=self.height-100,
            font=("苹方", 12)
        )
        self.chat_area.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.chat_area.configure(state='disabled')

        # 输入框框架
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        # 用户输入组件
        self.user_input = ttk.Entry(
            self.input_frame,
            width=60,
            font=("苹方", 12)
        )
        self.user_input.pack(side=tk.LEFT, padx=5, pady=5)
        self.user_input.bind("<Return>", lambda event: self.send_message())

        # 发送按钮
        self.send_btn = ttk.Button(
            self.input_frame,
            text="📎",
            command=self.send_message,
            width=8
        )
        self.send_btn.pack(side=tk.RIGHT, padx=5)

        # 布局配置
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def send_message(self) -> None:
        """处理消息发送事件
        
        执行以下操作：
        1. 获取输入框内容
        2. 显示用户消息到聊天区域
        3. 触发 AI 回复生成
        4. 清空输入框并滚动到底部
        """
        user_text = self.user_input.get()
        if not user_text.strip():
            return

        # 显示用户消息
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"\n{user_text}\n", ('user', 'right'))
        self.chat_area.configure(state='disabled')

        # 生成并显示 AI 回复
        ai_text = ai_response(user_text)
        self.show_ai_response(ai_text)

        # 清空输入框
        self.user_input.delete(0, tk.END)
        self.chat_area.see(tk.END)

    def show_ai_response(self, text: str) -> None:
        """显示 AI 回复到聊天区域

        Args:
            text (str): 需要显示的回复文本
        """
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END,str(get_response(text))+'\n', ('ai', 'left'))
        self.chat_area.configure(state='disabled')
if __name__ == '__main__':
    # 创建应用实例
    app = ChatApp()
    
    # 配置文本样式
    app.chat_area.tag_configure('user', foreground='lightgray')
    app.chat_area.tag_configure('ai', foreground='#2c7be5')
    app.chat_area.tag_configure('right', justify='right')
    app.chat_area.tag_configure('left', justify='left')
    
    # 启动主循环
    app.root.mainloop()
