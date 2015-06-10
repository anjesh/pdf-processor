import subprocess
import os.path

"""
ideas from https://gist.github.com/godber/7692812
"""

class PdfToText:
    def __init__(self, filepath, pages, outputDir):
        self.filepath = filepath
        self.pages = pages
        self.output = {}
        self.outputDir = outputDir
        self.cmd = "pdftotext"        

    def extractPage(self, page):
        outputFileName = os.path.join(self.outputDir, str(page) + ".txt")
        cmdOutput = subprocess.call([self.cmd, "-f", str(page), "-l", str(page), self.filepath, outputFileName])

    def extractPages(self):
        for page in range(1, self.pages+1):
            self.extractPage(page)



