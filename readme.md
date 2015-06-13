Scanned vs Structured PDF Processor
====================================

The script identifies whether the given pdf is structured (text based) or scanned one. 
If it's the text based pdf, it uses `pdftotext` tool to extract the text content and saves pages in the given folder. It also separates the pdf into individual pdf pages using `pdfseparate`.

### Prerequisites

Make sure that `pdftotext`, `pdfinfo` and `pdfseparate` are installed in your computer. These utils are available in [poppler-utils](https://packages.debian.org/sid/poppler-utils).

### How it works

* Reads the pdf file
* Uses `pdfinfo` to get the total pages in the pdf and size
* Uses `pdftotext` to dump the text and compares the size of the extract text content. If the text content size is 500 bytes in average for each page, then it is structured otherwise scanned one.
* If the pdf is structured, then it uses `pdftotext` to extract the text content page-wise and puts the txt files in the `text` folder.
* If the pdf is non-structured i.e. scanned, then it uses Abbyy OCR service to extract the text content `TODO`
* Creates `stats.json` file with the following content (structured = false if scanned)

```json
{ "structured": true, "pages": 5 }
```

* Uses `pdfseparate` to extract each pdf page and saves in the `pages` folder.


### Test

Execute `bash runtest.sh` to run all above tests at once.

### Run

* Register in ABBYY and get application-id and password, copy `settings.config.bak` to `settings.config` and update application-id and password
* `python run.py` to see the options
* `python run.py -i tests/sample.pdf -o out` creates folder `out/text` with the extracted text files, `out/pages` with the separated pdf files and `out/stats.json`.

### TODO

* log the events
* handle exceptions




