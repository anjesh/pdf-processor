from PdfProcessor import *
import argparse
from datetime import datetime
import ConfigParser
import ProcessLogger
import traceback
from urllib2 import HTTPError, URLError

parser = argparse.ArgumentParser(description='Processes the pdf and extracts the text')
parser.add_argument('-l','--language', help='Language of input pdf file for transcription (english, french, spanish).', required=False, default="english")
parser.add_argument('-i','--infile', help='File path of the input pdf file.', required=True)
parser.add_argument('-o','--outdir', help='File name of the output csv file.', required=True)
results = parser.parse_args()
allowed_languages = ["english", "french", "spanish"]
pdfProcessor = ""
try:
    logger = ProcessLogger.getLogger('run')
    logger.info("Processing started at %s ", str(datetime.now()))
    logger.info("input: %s", results.infile)
    logger.info("outdir: %s", results.outdir)  
    if results.language.lower() not in allowed_languages:
        raise Exception("language should be one of english, spanish, or spanish")

    configParser = ConfigParser.RawConfigParser()
    configParser.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.config'))

    pdfProcessor = PDFProcessor(results.infile, results.outdir, results.language.lower())
    pdfProcessor.setConfigParser(configParser)
    pdfProcessor.writeStats()
    if pdfProcessor.isStructured():
        pdfProcessor.extractTextFromStructuredDoc()
    else:
        pdfProcessor.extractTextFromScannedDoc()
except URLError as e:
    logger.error("URLError: %s", e.reason);
    logger.debug(traceback.format_exception(*sys.exc_info()))
except HTTPError as e:
    logger.error("HTTPError: [%s] %s", e.code, e.reason);
    logger.debug(traceback.format_exception(*sys.exc_info()))
except OSError as e:
    logger.error("OSError: %s [%s] in %s", e.strerror, e.errno, e.filename);
    logger.debug(traceback.format_exception(*sys.exc_info()))
except Exception as e:
    logger.error("Exception: %s ", e);
    logger.debug(traceback.format_exception(*sys.exc_info()))
finally:
    logger.info("Processing ended at %s ", str(datetime.now()));
