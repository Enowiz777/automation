# pdf_merging.py

# Create a program that takes two ranges
from PyPDF2 import PdfFileReader, PdfFileWriter
from page_input_to_numbers import convert_to_num_list

def merge_pdfs(nums, path, output):
    pdf_writer = PdfFileWriter()

    for num in nums:
        pdf_reader = PdfFileReader(path)

        max_pages = pdf_reader.getNumPages()
        # Validate the range.
        if num < 0 or num > max_pages:
            raise Exception("You are out of range!")
        # Need to raise an error.
        
        # Add each page to the writer object
        pdf_writer.addPage(pdf_reader.getPage(num))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    
    # Receive range
    path = './pdf/1.pdf'
    pdf_range = input("Please enter the page range: (ex: 1-5)")
    nums = convert_to_num_list(pdf_range)
    merge_pdfs(nums,path, output='merged.pdf')