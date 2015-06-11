from PdfProcessor import *
import argparse

parser = argparse.ArgumentParser(description='Processes the pdf and extracts the text')
parser.add_argument('-i','--infile', help='File path of the input pdf file.', required=True)
parser.add_argument('-o','--outdir', help='File name of the output csv file.', required=True)
results = parser.parse_args()

pdfProcessor = PDFProcessor(results.infile, results.outdir)
if pdfProcessor.isStructured():
    pdfProcessor.extractTextFromStructuredDoc()
else:
    pdfProcessor.extractTextFromScannedDoc()
pdfProcessor.separatePdfPages()
pdfProcessor.writeStats()


