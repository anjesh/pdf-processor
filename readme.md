Scanned and Structured PDF Processor
====================================

The script identifies whether the given pdf is structured (text based) or scanned one. 
If it's the text based pdf, it uses `pdftotext` tool to extract the text content and saves pages in the given folder. It also separates the pdf into individual pdf pages using `pdfseparate`.

### Prerequisites

Make sure that `pdftotext`, `pdfinfo` and `pdfseparate` are installed in your computer. These utils are available in [poppler-utils](https://packages.debian.org/sid/poppler-utils).

### Test

Execute `bash runtest.sh` to run all above tests at once.

### Run

* `python run.py` to see the options
* `python run.py -i tests/sample.pdf -o out` creates folder out/text with the extracted text files and `stats.json` with the following information (if the pdf is structured)

```json
{ "structured": true, "pages": 5 }
```




