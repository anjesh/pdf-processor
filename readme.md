Scanned and Structured PDF Processor
====================================

The script identifies whether the given pdf is structured (text based) or scanned one. 
If it's the text based pdf, it uses pdftotext linux tool to extract the page content and puts in the given folder. 

### Prerequisites

Make sure that `pdftotext` and `pdfinfo` are installed in your computer

### Test

Execute `bash runtest.sh` to run all above tests at once.

### Run

* `python run.py` to see the options
* `python run.py -i tests/sample.pdf -o out` creates folder out/text with the extracted text files and out/stats.json with the metainfo




