import subprocess
import os.path
import sys


class PdfTkSeparate:
    def __init__(self, infilepath, outdir):
        """
        wrapper around 'pdftk' to extract the text from the pdf
        """
        self.infilepath = infilepath
        self.outdir = outdir
        self.cmd = "pdftk"
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

    def extractPages(self):
        cmdOutput = subprocess.call([self.cmd, self.infilepath, 'burst', 'output', os.path.join(self.outdir, "%d.pdf")])
        return cmdOutput