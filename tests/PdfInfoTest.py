#!/usr/local/bin/python

import unittest
import sys
import os.path
from pdftools.PdfInfo import *

class PdfInfoTest(unittest.TestCase):
    def setUp(self):
        pass

    def testPdfPages(self):
        pdfInfo = PdfInfo('tests/sample.pdf')
        pdfInfo.process()
        self.assertEqual(pdfInfo.getPages(), 5)
        self.assertEqual(pdfInfo.getFileSizeInBytes(), 81691)

