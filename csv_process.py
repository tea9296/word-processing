import chardet
import csv


def change_encoding(input_file_path, output_file_path, desired_encoding):

    # Detect the encoding of the file
    with open("docs/panas/MTP訪談紀錄.csv", 'rb') as file:
        result = chardet.detect(file.read())

    original_encoding = result['encoding']

    # Read the original file
    with open(input_file_path,
              mode='r',
              encoding=original_encoding,
              newline='') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # Write to a new file with the desired encoding
    with open(output_file_path,
              mode='w',
              encoding=desired_encoding,
              newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)
    print("success")
    return


# original_encoding = 'Windows-1252'  # Example: 'cp950', 'ISO-8859-1', etc.
# desired_encoding = 'utf-8'

# input_file_path = "docs/panas/MTP訪談紀錄.csv"
# output_file_path = "docs/panas/MTP訪談紀錄2.csv"  # Can be the same as input_file_path to overwrite

# # Read the original file
# with open(input_file_path, mode='r', encoding=original_encoding,
#           newline='') as infile:
#     reader = csv.reader(infile)
#     rows = list(reader)

# # Write to a new file with the desired encoding
# with open(output_file_path, mode='w', encoding=desired_encoding,
#           newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerows(rows)

# ####
