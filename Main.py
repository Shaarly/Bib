import wx
import NewWindow


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Books', size=(600, 400))
        panel = wx.Panel(self)

        wx.StaticText(panel, label='Login:', style=wx.ALIGN_LEFT, pos=(5, 8))
        wx.StaticText(panel, label='Hasło:', style=wx.ALIGN_LEFT, pos=(5, 38))
        self.txtUser = wx.TextCtrl(panel, pos=(50, 5))
        self.txtPass = wx.TextCtrl(panel, pos=(50, 35))
        self.staticAlert = wx.StaticText(panel, label='', style=wx.ALIGN_CENTER, pos=(5, 120))

        my_btn = wx.Button(panel, label='Zaloguj', pos=(70, 65))
        my_btn.Bind(wx.EVT_BUTTON, self.OnLogin)


    def OnLogin(self, event):
        txtUser = self.txtUser.GetValue()
        txtPass = self.txtPass.GetValue()
        if self.CheckUsers(txtUser, txtPass):
            self.staticAlert.SetLabel('Zalogowano')
            logged = NewWindow.NewWindow()
            logged.Show()
        else:
            self.staticAlert.SetLabel('Błąd logowania')


    def CheckUsers(self, username, password):
        UsersFile = open('users.txt', 'r')
        for line in UsersFile:
            x = line.split(':')
            user1 = x[0]
            pass1 = x[1]
            pass1 = pass1.rsplit('\n')
            pass1 = pass1[0]
            if user1 == username and pass1 == password:
                return True
        return False


def main():
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
