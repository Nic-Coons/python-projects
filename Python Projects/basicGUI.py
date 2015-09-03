import wx

class windowClass(wx.Frame):

    

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.Move((450,150))
        self.Show()
        self.basicGUI()

    def basicGUI(self):

        #setup
        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)


        



        #file button
        fileButton = wx.Menu()
            #submenu
        importItem = wx.Menu()
        importItem.Append(wx.ID_ANY, 'Import Document')
        importItem.Append(wx.ID_ANY, 'Import Image')
        importItem.Append(wx.ID_ANY, 'Import Video')
        fileButton.AppendMenu(wx.ID_ANY, 'Import', importItem)

        newItem = wx.Menu()
        newItem.Append(wx.ID_ANY, 'New Window')
        fileButton.AppendMenu(wx.ID_ANY, 'New Window', newItem)

            #endsubmenu
        
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+q')
        
        fileButton.AppendItem(exitItem)
        
        menuBar.Append(fileButton, '&File')
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)


        #edit button
        editButton = wx.Menu()
        noEditItem = editButton.Append(wx.ID_EDIT, 'Edit', 'Edit')
        menuBar.Append(editButton, '&Edit')
        editItem = wx.Menu()
        editItem.Append(wx.ID_ANY, 'Edit Size Down')
        editItem.Append(wx.ID_ANY, 'Edit Size Up')
        editButton.AppendMenu(wx.ID_ANY, 'Edit Size', editItem)



        #help button
        helpButton = wx.Menu()
        menuBar.Append(helpButton, '&Help')
        helpItem = wx.MenuItem(helpButton, wx.ID_HELP, 'Help\tCtrl+h')

       


        #wrap up
        
        self.Show(True)
        
    def Quit(self, e):
        self.Close()




def main():    
    app = wx.App()
    windowClass(None, title='epic window')
    app.MainLoop()
main()
