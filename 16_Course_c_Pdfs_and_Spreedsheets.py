# PDFs and Spreadsheets Puzzle Exercise
# Let's test your skills, the files needed for this puzzle exercise

# You will need to work with two files for this exercise and solve the following tasks:

# Task One: Use Python to extract the Google Drive link from the .csv file. 
# (Hint: Its along the diagonal from top left to bottom right).
# Task Two: Download the PDF from the Google Drive link
# (we already downloaded it for you just in case you 
#  can't download from Google Drive) and find the phone number that is in the document. 
#  Note: There are different ways of formatting a phone number!
# Task One: Grab the Google Drive Link from .csv File

import csv
data = open('find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

link_list = []
for row_num,data in enumerate(data_lines):
    link_list.append(data[row_num])
print(''.join(link_list))

link_str = ''
for row_num,data in enumerate(data_lines):
    link_str+=data[row_num]

print(link_str)    

import PyPDF2
f = open('Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfReader(f)
print(len(pdf.pages))

import re
pattern = r'\d{3}'
all_text = ''

for n in range(len(pdf.pages)):
    
    page = pdf.pages[n]
    page_text = page.extract_text()
    
    all_text = all_text+' '+page_text
for match in re.finditer(pattern,all_text):
    print(match)

import re
pattern = r'\d{3}.\d{3}.\d{4}' 
for n in range(len(pdf.pages)):
    
    page  = pdf.pages[n]
    page_text = page.extract_text()
    match = re.search(pattern,page_text)
    
    if match:
        print(match.group())    

