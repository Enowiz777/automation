# pdf_merging.py

from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for item in items:
        pdf_reader = PdfFileReader(item['path'])
        start = item['start']-1 # To match the starting index
        end = item['end'] # range() function will take care of the ending index.
        for page in range(start, end):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    
    # Receive range
    first_pdf_range = input("Please enter the page range: (ex: 1-5)")
    second_pdf_range = input("Please enter the page range:(ex: 1-5)")
    
    # Split the first range
    first_text = first_pdf_range.split("-")
    first_range_start = int(first_text[0])
    first_range_end = int(first_text[1])

    # Split the second range
    second_text = second_pdf_range.split("-")
    second_range_start = int(second_text[0])
    second_range_end = int(second_text[1])

    items = [
        {
            "path": './pdf/1.pdf',
            "start": first_range_start,
            "end": first_range_end
        }, 
        {   "path": './pdf/2.pdf',
            "start": second_range_start,
            "end": second_range_end
        }
    ]


    paths = ['./pdf/1.pdf','./pdf/2.pdf']
    merge_pdfs(items, output='merged.pdf')