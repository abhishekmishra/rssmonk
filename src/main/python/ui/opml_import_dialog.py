import wx
import db.feed

class OPMLImportDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        super(OPMLImportDialog, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((500, 150))
        self.SetTitle("Import Feeds from OPML file.")
        self.opml_file = None


    def InitUI(self):

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(pnl, label="OPML File:", size=(75, 25))

        browseButton = wx.Button(pnl, label='Browse')
        browseButton.Bind(wx.EVT_BUTTON, self.open_file)

        self.filePathCtrl = wx.TextCtrl(pnl, size=(300, 25))

        hbox1.Add(st1, flag=wx.EXPAND | wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL)
        hbox1.AddSpacer(5)
        hbox1.Add(self.filePathCtrl, flag=wx.EXPAND | wx.ALIGN_CENTER)
        hbox1.AddSpacer(5)
        hbox1.Add(browseButton, flag=wx.EXPAND | wx.ALIGN_CENTER)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(pnl, label='Import')
        closeButton = wx.Button(pnl, label='Cancel')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        # vbox.Add(pnl, proportion=1,
        #     flag=wx.ALL|wx.EXPAND, border=5)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER|wx.ALL, border=20)
        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, border=10)

        pnl.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

    def open_file(self, e):
        with wx.FileDialog(self, "Open OPML file", wildcard="OPML files (*.opml)|*.opml",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            self.choose_opml_file(pathname)

    def choose_opml_file(self, pathname):
        self.opml_file = pathname
        self.filePathCtrl.WriteText(pathname)

    def OnImport(self):
        pass

    def OnClose(self, e):
        self.Destroy()


# try:
#     with open(pathname, 'r') as file:
#         self.choose_opml_file(file)
# except IOError:
#     wx.LogError("Cannot open file '%s'." % pathname)
