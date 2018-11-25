import os
import webbrowser
from . import Cfrate
cfrate = Cfrate.cfrate

class main_class(cfrate):
    def __init__(self):
        super().__init__()

    def readtxt(self):
        try:
            fi = open(self.file,'r')
            url = fi.read()
            fi.close()
            return url
        except Exception as ex:
            print('could\'nt find folder')
            return None

    def writetxt(self):
        fi  = open(self.file,'w')
        url = input("enter the link to tha page you want opened: ")
        print(url,file = fi)
        fi.close()
        return url

    def change(self):
        self.url = self.writetxt()

    def setup(self):
        self.file = "url.txt"
        if '\\' in self.path:
            slash = '\\'
        else:
            slash ='/'
        path = self.path.split(slash)
        path.pop()
        self.path = slash.join(path)
        # print(self.path)
        os.chdir(self.path)
        self.url = self.readtxt()
        if not self.url:
            self.url = self.writetxt()

    def do(self):
        webbrowser.open(self.url)
def main():
    main_class()
