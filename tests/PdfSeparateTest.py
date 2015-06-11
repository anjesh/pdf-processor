#!/usr/local/bin/python

import unittest
import sys
import glob
import os

from PdfSeparate import *

class PdfSeparateTest(unittest.TestCase):
    def setUp(self):
        """
        create dir if not present, 
        delete files if dir present
        """
        self.outdir = "tests/out/separate"
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        else:
            files = glob.glob(self.outdir)
            for f in files:
                if os.path.isfile(f):
                    os.remove(f)

    def testStructuredPdfPageExtraction(self):
        pdfSeparate = PdfSeparate('tests/sample.pdf', self.outdir)
        pdfSeparate.extractPages()
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"1.pdf")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"2.pdf")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"3.pdf")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"4.pdf")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"5.pdf")))

def testScannedPdfPageExtraction(self):
        pdfSeparate = PdfSeparate('tests/sample-scanned.pdf', self.outdir)
        pdfSeparate.extractPages()
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"1.pdf")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"2.pdf")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"3.pdf")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"4.pdf")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"5.pdf")))

