def convert_to_num_list(input):
    final_list = []
    pdf_range = input

    # Data clean up 
    
    # spaces remove.
    pdf_range = pdf_range.strip()

    # semi colon at the end.
    if pdf_range[len(pdf_range)-1] == ";":
        pdf_range = pdf_range[:len(pdf_range)-1]

    # Split the data by comma
    num_semi_split = pdf_range.split(";")

    # Go through the splited array and find ones with a dash "-"

    for item in num_semi_split:
        
        if "-" in item:
            new_item = item.split("-")
            new_item_one = int(new_item[0])
            new_item_two = int(new_item[1])
            numbers_in_range = range(new_item_one, new_item_two + 1)
            for num in numbers_in_range:
                final_list.append(int(num))
        else:
            final_list.append(int(item))

    # Return the list of numbers
    return final_list
