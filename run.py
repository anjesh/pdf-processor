from PdfProcessor import *
import argparse
from datetime import datetime
import ConfigParser
import ProcessLogger

parser = argparse.ArgumentParser(description='Processes the pdf and extracts the text')
parser.add_argument('-i','--infile', help='File path of the input pdf file.', required=True)
parser.add_argument('-o','--outdir', help='File name of the output csv file.', required=True)
results = parser.parse_args()

logger = ProcessLogger.getLogger('run')
logger.info("Processing started at %s ", str(datetime.now()))
logger.info("input: %s", results.infile)
logger.info("outdir: %s", results.outdir)  


configParser = ConfigParser.RawConfigParser()
configParser.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.config'))

pdfProcessor = PDFProcessor(results.infile, results.outdir)
pdfProcessor.setConfigParser(configParser)
if pdfProcessor.isStructured():
    pdfProcessor.extractTextFromStructuredDoc()
else:
    pdfProcessor.extractTextFromScannedDoc()
pdfProcessor.writeStats()

logger.info("Processing ended at %s ", str(datetime.now()));
