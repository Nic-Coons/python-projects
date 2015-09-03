import wx
from shutil import *
import os
import glob

class Nicky(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,id,'Frame aka Window', size=(80,80))

        panel=wx.Panel(self)

        
        self.button=wx.Button(self, -1, 'Open', pos=(10,10))
        self.button.Bind(wx.EVT_BUTTON, self.ccopy)
        


    def ccopy(self, event):
        files = glob.glob(os.path.join('C:\\Users\\Nic\\Desktop\\folderA', '*.*'))
        for f in files:
            copy(f, 'C:\\Users\\Nic\\Desktop\\folderB')
            print f
           # os.remove(f)
            #rmtree('C:\\Users\\Nic\\Desktop\\folderA\\')
            #os.mkdir('C:\\Users\\Nic\\Desktop\\folderA\\')
            

if __name__=='__main__':
    app=wx.App()
    frame=Nicky(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
