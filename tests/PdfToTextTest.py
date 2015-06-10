#!/usr/local/bin/python

import unittest
import sys

from PdfToText import *

class PdfToTextTest(unittest.TestCase):
    def setUp(self):
        pass

    def testPdfPages(self):
        pdfToText = PdfToText('tests/sample.pdf', 5, "tests/out")
        pdfToText.extractPage(1)

    def testPdfAllPages(self):
        pdfToText = PdfToText('tests/sample.pdf', 5, "tests/out")
        pdfToText.extractPages()

    def testPdfPageScanned(self):
        pdfToText = PdfToText('tests/sample-scanned.pdf', 5, "tests/out")
        pdfToText.extractPage(2)
