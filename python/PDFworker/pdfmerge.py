# pdf_merging.py

# Create a program that takes two ranges
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(dict, output):
    pdf_writer = PdfFileWriter()

    for item in dict:
        path = item["path"]
        pages = item["pages"]
        print(path)
        print(pages)
        pdf_reader = PdfFileReader(path)
        max_pages = pdf_reader.getNumPages()
        
        for page_num in pages:
        # Validate the range;Need to raise an error.
            print(type(page_num))
            if page_num < 0 or page_num > max_pages:
                raise Exception("You are out of range!")
        
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page_num))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

# if __name__ == '__main__':
    
#     # Receive range
#     path = './pdf/1.pdf'
#     pdf_range = input("Please enter the page range: (ex: 1-5)")
#     nums = convert_to_num_list(pdf_range)
#     merge_pdfs(nums,path, output='merged.pdf')