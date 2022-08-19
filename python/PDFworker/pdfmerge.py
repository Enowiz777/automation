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
                print(page-1)
                pdf_writer.addPage(pdf_reader.getPage(page-1))

    # Write out the merged PDF.
    output = output + "/1.pdf"
    with open(output, 'wb') as out:
        pdf_writer.write(output)

# if __name__ == '__main__':
    
#     # Receive range
#     path = './pdf/1.pdf'
#     pdf_range = input("Please enter the page range: (ex: 1-5)")
#     nums = convert_to_num_list(pdf_range)
#     merge_pdfs(nums,path, output='merged.pdf')