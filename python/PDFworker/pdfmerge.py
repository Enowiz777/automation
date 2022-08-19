# pdf_merging.py

# Create a program that takes two ranges
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(list_of_dict, output):
    pdf_writer = PdfFileWriter()

    for dict in list_of_dict:
        path = dict["path"]
        pages = dict["pages"]
        pdf_reader = PdfFileReader(path)
        max_pages = pdf_reader.getNumPages()
        print(path, pages, max_pages)

        # Check each pages and 
        # Make sure that the page number is less than max_pages
        for page in pages:
            if page < 0 or page > max_pages:
                raise Exception("You are out of range!")
            else:
                pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF.
    with open(output, 'wb') as out:
        
        pdf_writer.write(out)

# if __name__ == '__main__':
    
#     # Receive range
#     path = './pdf/1.pdf'
#     pdf_range = input("Please enter the page range: (ex: 1-5)")
#     nums = convert_to_num_list(pdf_range)
#     merge_pdfs(nums,path, output='merged.pdf')