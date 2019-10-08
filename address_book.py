#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Sat Oct  5 13:31:42 2019
#

import wx
import sqlite3

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    conn_init = sqlite3.connect('address_book.db')
    cursor_init= conn_init.cursor()
    
    cursor_init.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='person';")
        
    if cursor_init.fetchone()[0] !=1 :
        cursor_init.execute('''CREATE TABLE person (fname Varchar, 
                                                lname Varchar,
                                                address Varchar,
                                                phone_no Varchar,
                                                email lname Varchar
                                                );''')

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
        self.button_submit.Bind(wx.EVT_BUTTON, self.ButtonSubmit)

        self.button_get = wx.Button(self, wx.ID_ANY, "Get")
        self.button_get.Bind(wx.EVT_BUTTON, self.ButtonGet)

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

    def ButtonSubmit(self,event):
        conn_sub = sqlite3.connect('address_book.db')
        cursor_sub = conn_sub.cursor()

        data=[]
        data.append(self.text_ctrl_ln.GetValue())
        data.append(self.text_ctrl_fn.GetValue())
        data.append(self.text_ctrl_address.GetValue())
        data.append(self.text_ctrl_phone_no.GetValue())
        data.append(self.text_ctrl_email.GetValue())

        cursor_sub.execute('insert into person values (?,?,?,?,?)', data)
        conn_sub.commit()
        conn_sub.close()
       

        self.text_ctrl_ln.Clear()
        self.text_ctrl_fn.Clear()
        self.text_ctrl_address.Clear()
        self.text_ctrl_phone_no.Clear()
        self.text_ctrl_email.Clear()

        
        

        

    def ButtonGet(self,event):
        conn_get = sqlite3.connect('address_book.db')
        cursor_get = conn_get.cursor()

        

        get_data=[]
        get_data.append(self.text_ctrl_ln.GetValue())
        if self.text_ctrl_ln.GetValue()!= "":
            self.text_ctrl_ln.Clear()


        get_data.append(self.text_ctrl_fn.GetValue())
        if self.text_ctrl_fn.GetValue() != "":
             self.text_ctrl_fn.Clear()

        get_data.append(self.text_ctrl_address.GetValue())
        if self.text_ctrl_address.GetValue() != "":
             self.text_ctrl_address.Clear()

        get_data.append(self.text_ctrl_phone_no.GetValue())
        if self.text_ctrl_phone_no.GetValue() != "":
             self.text_ctrl_phone_no.Clear()

        get_data.append(self.text_ctrl_email.GetValue())
        if self.text_ctrl_email.GetValue() != "":
            self.text_ctrl_email.Clear()

       

        for gd in get_data:
            if gd != "":
              
                for row in  cursor_get.execute('select lname,fname,address,phone_no,email from  person '):
                    self.text_ctrl_ln.AppendText(row[0])
                    self.text_ctrl_fn.AppendText(row[1])
                    self.text_ctrl_address.AppendText(row[2])
                    self.text_ctrl_phone_no.AppendText(row[3])
                    self.text_ctrl_email.AppendText(row[4])


        
        
        conn_get.commit()
        conn_get.close()

        

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
