import subprocess
import os.path

class PdfToText:
    def __init__(self, infilepath, pages, outdir):
        """
        wrapper around 'pdftotext' to extract the text from the pdf
        """
        self.infilepath = infilepath
        self.pages = pages
        self.outdir = outdir        
        self.cmd = "pdftotext"
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

    def dumpPages(self):        
        """
        dumps the content of the pdf in a single file, to check whether there are significant number of character to verify if it's the strcutured or not
        """
        filename = os.path.split(self.infilepath)[1].split(".")[0]        
        self.dumpedTextFilepath = os.path.join(self.outdir,  filename + ".txt")
        cmdOutput = subprocess.call([self.cmd, self.infilepath, self.dumpedTextFilepath])

    def extractPage(self, page):
        outputFileName = os.path.join(self.outdir, str(page) + ".txt")
        cmdOutput = subprocess.call([self.cmd, "-f", str(page), "-l", str(page), self.infilepath, outputFileName])

    def extractPages(self):
        """
        unlike dumppages, it extracts the content of every page in each file, and converts newline to linebreak
        """
        for page in range(1, self.pages+1):
            self.extractPage(page)
            outputFileName = os.path.join(self.outdir, str(page) + ".txt")
            with open(outputFileName, 'r') as infile:
                content = infile.read()            
            with open(outputFileName, 'w') as outfile:
                outfile.write(self.nl2br(content))

    def nl2br(self, s):
        return '<br />\n'.join(s.split('\n'))



