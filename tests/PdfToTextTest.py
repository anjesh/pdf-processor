#!/usr/local/bin/python

import unittest
import sys
import glob
import os

from PdfToText import *

class PdfToTextTest(unittest.TestCase):
    def setUp(self):
        """
        create dir if not present, 
        delete files if dir present
        """
        self.outdir = "tests/out/pdftotext"
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        else:
            files = glob.glob(self.outdir)
            for f in files:
                if os.path.isfile(f):
                    os.remove(f)

    def testStructuredPdfPage(self):        
        pdfToText = PdfToText('tests/sample.pdf', 5, self.outdir)
        pdfToText.extractPage(1)
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"1.txt")))

    def testScannedPdfPage(self):
        pdfToText = PdfToText('tests/sample-scanned.pdf', 5, self.outdir)
        pdfToText.extractPage(2)
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"2.txt")))

    def testStructuredPdfAllPagewise(self):
        pdfToText = PdfToText('tests/sample.pdf', 5, self.outdir)
        pdfToText.extractPages()
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"1.txt")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"2.txt")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"3.txt")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"4.txt")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"5.txt")))

    def testStructuredPdfAllPagesDump(self):
        pdfToText = PdfToText('tests/sample.pdf', 5, self.outdir)
        pdfToText.dumpPages()
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"sample.txt")))

