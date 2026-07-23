import wx

app = wx.App()
frame = wx.Frame(None, title="Wordle", size=(500, 600))

panel=wx.Panel(frame)

title = wx.StaticText(panel, label="WORDLE")

font = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
title.SetFont(font)

sizer=wx.BoxSizer(wx.VERTICAL)
sizer.Add(title,0,wx.ALIGN_CENTER|wx.TOP, 20)
panel.SetSizer(sizer)

frame.Show()
app.MainLoop()