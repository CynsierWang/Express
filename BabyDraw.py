# -*- coding: utf-8 -*-
import Tkinter as tk
import Fetch
import Feed

top = tk.Tk()
top.title("LUM Express")
BtnFetch = tk.Button(top, text="我要取快递", command=Fetch.FetchFunction)
BtnFetch.pack()
BtnFeed = tk.Button(top, text="我不取快递", command=Feed.FeedFunction)
BtnFeed.pack()
top.mainloop()