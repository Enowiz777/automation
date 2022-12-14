from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

def pdf2txt(inPDFfile, outTXTFile): 
    inFile = open(inPDFfile, 'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr, retData,laparams = LAParams())
    interpreter = PDFPageInterpreter(resMgr, TxtConverter)
    
    for page in PDFPage.get_pages(inFile): 
        interpreter.process_page(page)
        
    txt = retData.getvalue()
    with open(outTXTFile, 'w') as f: 
         f.write(txt)
   
inPDFfile = "./pdf/2.pdf" # your file path
outTXTFile = "sample.txt" # what ever the name you want enjoy!
pdf2txt(inPDFfile, outTXTFile)
 