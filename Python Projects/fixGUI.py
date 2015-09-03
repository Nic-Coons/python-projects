import wx

class windowClass(wx.Frame):

    

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.Move((450,150))
        self.Show()
        self.basicGUI()

    def basicGUI(self):

        #setup
        loser = ''
        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)

        
        #namebox
        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome', 'Nic')
        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()
        
        

        #yesNobox
        yesNoBox = wx.MessageDialog(None, 'Do you want to build a snowman?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        if yesNoAnswer == wx.ID_NO:
            userName = 'Snow Hating Loser!'

        #colorbox
        chooseOneBox = wx.SingleChoiceDialog(None, 'Pick a color', 'Colors',
                                             ['green', 'blue', 'orange', 'red'])
        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        #panel
        wx.TextCtrl(panel, pos=(35, 50), size=(320, 100))
        panel.SetBackgroundColour('white')

        aweText = wx.StaticText(panel, -1, 'Awesome text', (150, 10))
        aweText.SetForegroundColour('yellow')
        aweText.SetBackgroundColour('black')

        myText = wx.StaticText(panel, -1, 'Welcome '+userName+'!', (150, 30))
        myText.SetForegroundColour(favColor)
        myText.SetBackgroundColour('black')


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
        exitItem.SetBitmap(wx.Bitmap('sad.bmp'))
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

        #toolbar
        toolBar = self.CreateToolBar()
        quitToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Quit',
                                              wx.Bitmap('sad.bmp'))
        toolBar.Realize()


        #wrap up
        self.SetTitle('Welcome ' +userName + loser)
        self.Show(True)
        
    def Quit(self, e):
        self.Close()




def main():    
    app = wx.App()
    windowClass(None, title='epic window')
    app.MainLoop()
main()
