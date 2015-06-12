#!/usr/local/bin/python

import unittest
import sys
import os.path
import glob
import ConfigParser
from pdftools.PdfSeparate import *
from abbyy.AbbyyPdfTextExtractor import *

class AbbyyPdfTextExtractorTest(unittest.TestCase):
    def setUp(self):
        self.outdir = "tests/out/abbyy/text"
        self.indir = "tests/out/abbyy/pdf"
        self.createOrCleanDir(self.outdir)
        self.createOrCleanDir(self.indir)
        self.configParser = ConfigParser.RawConfigParser()
        self.configParser.read('settings.config')


    def createOrCleanDir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            files = glob.glob(directory)
            for f in files:
                if os.path.isfile(f):
                    os.remove(f)


    def testScannedPdfPage(self):
        pdfSeparate = PdfSeparate('tests/sample-scanned.pdf', self.indir)
        pdfSeparate.extractPages()
        self.assertTrue(os.path.isfile(os.path.join(self.indir,"1.pdf")))

        abbyyPdf = AbbyyPdfTextExtractor(self.indir, self.outdir, 5, "english")
        abbyyPdf.setApplicationCredentials(self.configParser.get('abbyy','appid'), self.configParser.get('abbyy','password'))
        abbyyPdf.processPdfPage(1);
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"1.txt")))

    def testScannedPdfPages(self):
        pdfSeparate = PdfSeparate('tests/sample-scanned-1.pdf', self.indir)        
        pdfSeparate.extractPages()
        self.assertTrue(os.path.isfile(os.path.join(self.indir,"1.pdf")))

        abbyyPdf = AbbyyPdfTextExtractor(self.indir, self.outdir, 2, "english")
        abbyyPdf.setApplicationCredentials(self.configParser.get('abbyy','appid'), self.configParser.get('abbyy','password'))
        abbyyPdf.extractPages();
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"1.txt")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"2.txt")))
