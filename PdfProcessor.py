from os import listdir
import os.path
import json
from pdftools.PdfInfo import *
from pdftools.PdfToText import *
from pdftools.PdfSeparate import *

class PDFProcessor:
    def __init__(self, filePath, outputDir):
        self.filePath = filePath
        self.outputDir = outputDir
        self.textContentSize = 0
        self.totalPages = 0
        self.process()
        self.processToCheckStructured()

    def setConfigParser(self, configParser):
        self.configParser = configParser

    def process(self):
        pdfInfo = PdfInfo(self.filePath)
        self.totalPages = pdfInfo.getPages()
        self.fileSize = pdfInfo.getFileSizeInBytes()
        self.separatePdfPages()

    def processToCheckStructured(self):
        """
        dumps the entire pdf to text to get the size of the content
        """
        pdfToText = PdfToText(self.filePath, self.totalPages, self.outputDir)
        pdfToText.dumpPages()
        self.textContentSize += os.path.getsize(pdfToText.dumpedTextFilepath)

    def isStructured(self):
        """
        assuming that text content should be at least 50 bytes in average in each page to say 
        that the pdf is structured
        """
        return True if self.textContentSize > (self.totalPages*50) else False

    def writeStats(self):
        stats = {"pages": self.totalPages, "structured": self.isStructured()}
        with open(os.path.join(self.outputDir,'stats.json'),'w') as outfile:
            json.dump(stats, outfile)

    def separatePdfPages(self):
        pdfSeparate = PdfSeparate(self.filePath, os.path.join(self.outputDir,'pages'))
        pdfSeparate.extractPages()

    def extractTextFromStructuredDoc(self):
        """
        creates "text" dir to dump the extracted pages
        """
        pdfToText = PdfToText(self.filePath, self.totalPages, os.path.join(self.outputDir,'text'))
        pdfToText.extractPages()

    def extractTextFromScannedDoc(self):
        """
        makes api calls 
        """
        abbyyPdf = AbbyyPdfTextExtractor(os.path.join(self.outputDir,'pages'), os.path.join(self.outputDir,'text'), self.totalPages, "english")
        abbyyPdf.setApplicationCredentials(self.configParser.get('abbyy','appid'), self.configParser.get('abbyy','password'))
        abbyyPdf.extractPages();




