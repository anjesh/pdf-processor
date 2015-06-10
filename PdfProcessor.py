from os import listdir
import os.path
from PdfInfo import *
from PdfToText import *

class PDFProcessor:
    def __init__(self, filePath, outputDir):
        self.filePath = filePath
        self.outputDir = outputDir
        self.totalPages = 0
        self.structured = False
        pass

    def process(self):
        pdfInfo = PdfInfo(self.filePath)
        self.totalPages = pdfInfo.getPages()
        pdfToText = PdfToText(self.filePath, self.totalPages, self.outputDir)
        pdfToText.extractPages()

    def smellExtractedPages(self):
        for f in listdir(self.outputDir):
            if os.path.isfile(os.path.join(self.outputDir, f)):
                txt = open(os.path.join(self.outputDir, f))

    def isStructure(self):
        return True if self.structured else False

    def __init__(self, filePath):
        self.cmd = ''



