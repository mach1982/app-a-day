#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Sat Oct  5 13:31:42 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.text_ctrl_ln = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_fn = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_address = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_phone_no = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_email = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_submit = wx.Button(self, wx.ID_ANY, "Submit")
        self.button_get = wx.Button(self, wx.ID_ANY, "Get")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Address Book")
        self.text_ctrl_ln.SetMinSize((200, 30))
        self.text_ctrl_fn.SetMinSize((200, 30))
        self.text_ctrl_address.SetMinSize((200, 30))
        self.text_ctrl_phone_no.SetMinSize((200, 30))
        self.text_ctrl_email.SetMinSize((200, 30))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(6, 4, 3, 3)
        label_ln = wx.StaticText(self, wx.ID_ANY, "Lastname:")
        grid_sizer_1.Add(label_ln, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_ln, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_fn = wx.StaticText(self, wx.ID_ANY, "Firstname:")
        grid_sizer_1.Add(label_fn, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_fn, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_address = wx.StaticText(self, wx.ID_ANY, "Address:")
        grid_sizer_1.Add(label_address, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_address, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_phone_no = wx.StaticText(self, wx.ID_ANY, "Phone No:")
        grid_sizer_1.Add(label_phone_no, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_phone_no, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_email = wx.StaticText(self, wx.ID_ANY, "E-mail:")
        grid_sizer_1.Add(label_email, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_email, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_submit, 0, 0, 0)
        grid_sizer_1.Add(self.button_get, 0, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
