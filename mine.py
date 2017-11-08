from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal
import pandas as pd

base = {'contents': [], 'parent': []}

document = open('test.pdf', 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

pd.set_option('display.max_colwidth', -1)

for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for element in layout:
        if isinstance(element, LTTextBoxHorizontal):
            for text in element:
                if isinstance(text, LTTextLineHorizontal) and text.get_text() != " \n":
                    base['contents'].append(text.get_text())
                    base['parent'].append((element.index, element.__class__))

base = pd.DataFrame(data=base)