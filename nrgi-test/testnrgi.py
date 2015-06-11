import urllib2
import sys
import os.path
import csv
import urlparse
sys.path.append('../')
from PdfProcessor import *

"""
tests all the existing pdfs whether it's structured or not
"""

def download_file(download_url, outfile):
    response = urllib2.urlopen(download_url)
    file = open(outfile, 'w')
    file.write(response.read())
    file.close()

statusFile = open('pdf-status.csv', 'w')
csvFile = csv.writer(statusFile, delimiter=',')
with open("nrgi-pdf-list.txt") as pdfLinksList:
    for pdfLink in pdfLinksList:
        pdfName = os.path.basename(urlparse.urlsplit(pdfLink.strip()).path)
        outfile = os.path.join('pdf', pdfName)
        if not os.path.isfile(outfile):
            print "downloading ", pdfLink
            download_file(pdfLink.strip(), outfile)
        pdfProcessor = PDFProcessor(outfile, 'out')
        isStructured = "Structured" if pdfProcessor.isStructured() else "Scanned"
        print pdfName, ":", isStructured
        csvFile.writerow([pdfName, isStructured])
statusFile.close()        


        



    