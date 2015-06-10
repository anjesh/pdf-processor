import subprocess

"""
ideas from https://gist.github.com/godber/7692812
"""

class PdfInfo:
    def __init__(self, filepath):
        self.filepath = filepath
        self.output = {}
        self.cmd = "pdfinfo"
        self.process()

    def process(self):
        labels = ['Title', 'Author', 'Creator', 'Producer', 'CreationDate', \
                'ModDate', 'Tagged', 'Pages', 'Encrypted', 'Page size', \
                'File size', 'Optimized', 'PDF version']        
        cmdOutput = subprocess.check_output([self.cmd, self.filepath])
        for line in cmdOutput.splitlines():
            for label in labels:
                if label in line:
                    self.output[label] = self.extract(line)
    
    def extract(self, row):
        return row.split(':', 1)[1].strip()

    def getPages(self):
        return int(self.output['Pages'])

    def getFileSizeInBytes(self):
        return int(self.output['File size'][:-5].strip())

