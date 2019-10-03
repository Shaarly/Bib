import wx


class BooksList(wx.ListCtrl):
    def __init__(self, parent, id):
        super().__init__(parent, id, pos=(5, 5), size=(400, 300))
        self.SetForegroundColour(wx.Colour(255, 255, 255))
        self.SetBackgroundColour(wx.Colour(0, 89, 179))
        self.LoadBooks()
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelect)


    def OnSelect(self, event):
        print('haha')


    def LoadBooks(self):
        BooksFile = open('books.txt', 'r')
        for line in BooksFile:
            line = line.rsplit('\n')
            line = line[0]
            print(line)
            self.InsertItem(self.GetItemCount(), line)


class NewWindow(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Logged In', size=(600, 400))
        panel = wx.Panel(self)

        lista = BooksList(panel, 1)
