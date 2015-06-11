import subprocess
import os.path

class PdfSeparate:
    def __init__(self, infilepath,outdir):
        """
        wrapper around 'pdftotext' to extract the text from the pdf
        """
        self.infilepath = infilepath
        self.outdir = outdir        
        self.cmd = "pdfseparate"
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

    def extractPages(self):
        cmdOutput = subprocess.call([self.cmd, self.infilepath, os.path.join(self.outdir, "%d.pdf")])
        