#!/usr/local/bin/python

import unittest
import sys
import os.path
import os
import glob
import ConfigParser

from PdfProcessor import *

class PdfProcessorTest(unittest.TestCase):
    def setUp(self):
        """
        create dir if not present, 
        delete files if dir present
        """
        self.outdir = "tests/out/pdfprocessor"
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        else:
            files = glob.glob(self.outdir)
            for f in files:
                if os.path.isfile(f):
                    os.remove(f)
        self.configParser = ConfigParser.RawConfigParser()
        self.configParser.read('settings.config')


    def testStructuredPdf(self):
        pdfProcessor = PDFProcessor('tests/sample.pdf', self.outdir)
        self.assertTrue(pdfProcessor.isStructured())

    def testScannedPdf(self):
        pdfProcessor = PDFProcessor('tests/sample-scanned.pdf', self.outdir)
        self.assertFalse(pdfProcessor.isStructured())

    def testScannedPdfStats(self):
        pdfProcessor = PDFProcessor('tests/sample-scanned.pdf', self.outdir)
        pdfProcessor.writeStats()
        with open(os.path.join(self.outdir,"stats.json")) as json_file:
            json_data = json.load(json_file)
            self.assertFalse(json_data['structured'])            
            self.assertEqual(json_data['pages'], 5)            

    def testStructuredPdfStats(self):
        pdfProcessor = PDFProcessor('tests/sample.pdf', self.outdir)
        pdfProcessor.writeStats()
        with open(os.path.join(self.outdir,"stats.json")) as json_file:
            json_data = json.load(json_file)
            self.assertTrue(json_data['structured'])            
            self.assertEqual(json_data['pages'], 5)            

    def testStructuredPdfExtractPages(self):
        pdfProcessor = PDFProcessor('tests/sample.pdf', self.outdir)
        self.assertTrue(pdfProcessor.isStructured())
        pdfProcessor.extractTextFromStructuredDoc()
        self.assertTrue(os.path.isdir(os.path.join(self.outdir,"text")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"text","1.txt")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"text","5.txt")))

    def testSeparatePdfPages(self):
        pdfProcessor = PDFProcessor('tests/sample.pdf', self.outdir)
        pdfProcessor.separatePdfPages()
        self.assertTrue(os.path.isdir(os.path.join(self.outdir,"pages")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"pages","1.pdf")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"pages","5.pdf")))

    def testScannedPdfExtractPages(self):
        pdfProcessor = PDFProcessor('tests/sample-scanned-1.pdf', self.outdir)
        pdfProcessor.setConfigParser(self.configParser)        
        self.assertFalse(pdfProcessor.isStructured())
        pdfProcessor.extractTextFromScannedDoc()
        self.assertTrue(os.path.isdir(os.path.join(self.outdir,"text")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"text","1.txt")))
        self.assertTrue(os.path.isfile(os.path.join(self.outdir,"text","2.txt")))
