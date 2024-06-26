from tkinter import *
from chat import get_response,bot_name

BG_GRAY="#ABB289"
BG_COLOUR="#17202A"
TEXT_COLOUR="#EAECEE"

FONT= "Helvetica 14"
FONT_BOLD="Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window=Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False,height=False)
        self.window.configure(width=480,height=False)
    



if __name__ =="__main__":
    app=ChatApplication()
    app.run()