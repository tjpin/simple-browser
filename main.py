import sys
import requests

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType


ui, baseClass = loadUiType("ui/browser.ui")


class PythonBrowser(QMainWindow, ui):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self._url = "https://instagram.com"
        self.engine.setUrl(self._url)
        
        self.events()
    
    def events(self):
        self.engine.urlChanged.connect(lambda link: self.setCurrentUrl(link.url()))
        self.engine.iconUrlChanged.connect(lambda icon: self.setUrlIcon(icon.url()))
        self.engine.titleChanged.connect(lambda title: self.setCurrentTile(title))
        self.searchBox.returnPressed.connect(lambda: self.openNewUrl(self.searchBox.text()))
    
    def setCurrentUrl(self, url):
        self.statusBar.showMessage(url)
    
    def validateUrl(self, text: str):
        try:
            if "https://" not in text and text.find(".") == -1:
                return "https://google.com/search?q={}".format(text)
            if "https://" in text:
                return text
            return "https://{}".format(text)
        except Exception as e:
            pass
        
    def setCurrentTile(self, title):
        self.currentUrl.setText(title)
    
    def setUrlIcon(self, url):
        self.urlIcon.setIcon(self.getIconFromUrl(url))
            
    def getIconFromUrl(self, url):
        ''' Get icon from url'''
        try:
            pixmap = QPixmap()
            response = requests.get(url)
            pixmap.loadFromData(response.content)
            return pixmap
        except:
            ''' If no icon is loaded return empty pixmap'''
            return QPixmap()

    def openNewUrl(self, url):
        self.engine.load(self.validateUrl(url))

    def geBack(self):
        # todo
        pass
    
    def goFoeward(self):
        # todo
        pass
        


if __name__ == "__main__":
    app = QApplication([])
    win = PythonBrowser()
    win.show()
    sys.exit(app.exec())