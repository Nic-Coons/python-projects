import wx

import time
from datetime import datetime
import glob, os
import shutil


global rootFolder
global destFolder


now = datetime.utcnow()
rootFolder = os.getcwd()
destFolder = os.getcwd()
########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File mover", size=(160,300))
        self.Move((650,150))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour('white')
        #button1
        btn = wx.Button(panel, label="Set Root Folder", pos=(0,10))
        btn.Bind(wx.EVT_BUTTON, self.onOpenDir)
        roots = wx.StaticText(panel, -1, label=rootFolder, pos=(0,50))
       # roots.SetForegroundColour('red')
        #button2
        btn2 = wx.Button(panel, label="Set Destination Folder", pos=(0, 100))
        btn2.Bind(wx.EVT_BUTTON, self.onSelectDir)
       # broots = wx.StaticText(panel, -1, 'Destination Folder: ' + destFolder, (0, 150))
       # broots.SetForegroundColour('red')
        #button3
        submitter = wx.Button(panel, label="Transfer Files", pos=(0,200))
        submitter.Bind(wx.EVT_BUTTON, self.submitFiles)



        
 
     #----------------------------------------------------------------------
    def onOpenDir(self, event):
        dlg = wx.DirDialog(
            self, message="Choose a Folder",
            style=wx.OPEN | wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            print dlg.GetPath()
            global rootFolder
            rootFolder = dlg.GetPath()
            
        dlg.Destroy()

    #----------------------------------------------------------------------
    def onSelectDir(self, event):
        dial = wx.DirDialog(
            self, message="Choose a Folder",
            style=wx.OPEN | wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR
            )
        if dial.ShowModal() == wx.ID_OK:
            print dial.GetPath()
            global destFolder
            destFolder = dial.GetPath()
            
        dial.Destroy()
    #----------------------------------------------------------------------
    def submitFiles(self, event):
        print 'hi'
        print rootFolder
        print destFolder
        os.chdir(rootFolder)
        for file in glob.glob("*.*"):    
            print file
            dateone = os.path.getctime(file)
            datetwo = datetime.fromtimestamp(dateone)
            nudate = str(now - datetwo)
            print nudate
            if 'day' in nudate:
                print 'yes'              
            else:
                print 'no'
                shutil.move(file, 'C:\\Users\\Nic\\Desktop\\folderB')
    #----------------------------------------------------------------------

 
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
