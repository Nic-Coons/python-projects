from bs4 import BeautifulSoup
import requests
import wx




class window(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "HTML Scraper", size=(400,500))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour('#11dd55')
        text = wx.StaticText(panel, -1, "Please Enter a url:", (100, 50), (160, -1), wx.ALIGN_CENTER)
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text.SetFont(font)
        self.basicText = wx.TextCtrl(panel, -1, "http://", size=(175, -1), pos=(100,100))
        self.basicText.SetInsertionPoint(0)
        text = wx.StaticText(panel, -1, "Choose search parameters:", (100, 140), (160, -1), wx.ALIGN_CENTER)
        self.linkChoice = wx.RadioButton(panel, label="Links", pos=(100,160))
        self.textChoice = wx.RadioButton(panel, label="Text", pos=(160,160))
        self.replaceChoice = wx.RadioButton(panel, label="Replace", pos=(220,160))
        button = wx.Button(panel, label='Submit', pos=(140,200))
        button.Bind(wx.EVT_BUTTON, self.urllookup)
        
        
        



    def urllookup(self, event):
        if self.textChoice.GetValue() == True:
            try:
                url = self.basicText.GetValue()
                r = requests.get("http://"+url)
                data = r.text
                soup = BeautifulSoup(data, "html.parser")
                for link in soup.find_all('p'):
                    print link.text
            except Exception as e:
                print(str(e))
        if self.linkChoice.GetValue() == True:
            try:
                url = self.basicText.GetValue()
                r = requests.get("http://"+url)
                data = r.text
                soup = BeautifulSoup(data, "html.parser")
                for link in soup.find_all('a'):
                    print link.text, link.get('href')
            except Exception as e:
                print(str(e))


if __name__ == "__main__":
    app = wx.App(False)
    frame = window()
    frame.Show()
    app.MainLoop()
