import re
from datetime import datetime
import copy

class PdfProcessingStatus:
    def __init__(self):
        self.lines = []
        pass 

    def add(self, logline):
        self.lines.append(logline)

    def printStatus(self):
        print "PDF Type, Total Pages, Duration"
        for l, line in enumerate(self.lines):
            line = self.lines[l]
            print line.pdfType, ",", line.totalPages, ",", line.endTime - line.startTime

class LogLine:
    def __init__(self):
        self.clean()

    def clean(self):
        self.startTime = 0
        self.endTime = 0
        self.pdfType = 0
        self.totalPages = 0        

    def process(self, line):
        self.line = line
        if self.checkStart():
            return
        elif self.checkStatsJson():
            return
        elif self.checkEnd():
            return
 
    def checkStart(self):
        #2015-07-08 06:04:17,856 run INFO - Processing started at 2015-07-08 06:04:17.856930
        m = re.findall('([0-9-: ]*),[0-9]*[^-]*- Processing started', self.line)
        if m and m[0]:
            self.startTime = datetime.strptime(m[0], '%Y-%m-%d %H:%M:%S')
            return True
        return False
        
    def checkEnd(self):
        #2015-07-08 06:04:17,856 run INFO - Processing started at 2015-07-08 06:04:17.856930
        m = re.findall('([0-9-: ]*),[0-9]*[^-]*- Processing ended', self.line)
        if m and m[0]:
            self.endTime = datetime.strptime(m[0], '%Y-%m-%d %H:%M:%S')
            return True
        return False

    def checkStatsJson(self):
        #2015-07-08 06:04:18,639 PDFProcessor INFO - Writing {"status": "Structured", "pages": 10} to stats.json
        m = re.findall('([0-9-: ]*),[0-9]*[^-]*- Writing {"status": "([^"]*)", "pages": ([0-9]*)', self.line)
        if m and m[0]:
            self.pdfType = m[0][1]
            self.totalPages = m[0][2]
            return True
        return False

    def isDone(self):
        if self.endTime:
            return True
        return False;


pdfProcessingStatus = PdfProcessingStatus()
with open('processing.log') as f:
    logline = LogLine()
    for line in f:
        logline.process(line)
        if logline.isDone():
            pdfProcessingStatus.add(copy.copy(logline))
            logline.clean()
pdfProcessingStatus.printStatus()            