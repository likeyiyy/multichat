#!/usr/bin/env python
# coding=utf-8
import wx
class multiChatGui(wx.Frame):
    def __init__(self,send=None,view_context=None,view_list=None):
        self.app = wx.App()
        self.win = wx.Frame(None, title="MultiChat",size=(480,400))
        self.bkg = wx.Panel(self.win)
        self.sendbutton = wx.Button(self.bkg,label="send")
        self.context    = wx.TextCtrl(self.bkg,value="hello world",
                                      style=wx.TE_READONLY|wx.TE_MULTILINE)
        self.list       = wx.TextCtrl(self.bkg,value="sira\nsirb\nsirc\n",
                                      style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.info       = wx.TextCtrl(self.bkg,style=wx.TE_MULTILINE)

        # info + send 
        self.hbox1      = wx.BoxSizer()
        self.hbox1.Add(self.info,proportion=1,flag=wx.EXPAND)
        self.hbox1.Add(self.sendbutton,proportion=0,flag=wx.RIGHT)

        # text
        # info + send
        self.vbox1      = wx.BoxSizer(wx.VERTICAL)
        self.vbox1.Add(self.context,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP)
        self.vbox1.Add(self.hbox1,proportion=0,flag=wx.EXPAND)

        # text        | list
        # info + send |
        self.hbox2      = wx.BoxSizer()
        self.hbox2.Add(self.vbox1,proportion=2,flag=wx.EXPAND|wx.ALL,border=5)
        self.hbox2.Add(self.list, proportion=1,flag=wx.RIGHT|wx.EXPAND|wx.BOTTOM|wx.TOP,border=5)
        self.bkg.SetSizer(self.hbox2)
        self.send = send
        self.view_context = view_context
        self.view_list    = view_list
        self.win.Show()
    def display(self):
        self.app.MainLoop()



