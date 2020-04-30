import os

import PyPDF2

pdffile =[]

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdffile.append(filename)

pdffile.sort()

pdf_write = PyPDF2.PdfFileWriter()

for filename in pdffile:
	obj = open(filename,'rb')
	read = PyPDF2.PdfFileWriter(obj)
	for pgn in range(1,read.numPages):
		pgo = read.getPage(pgn)
		pdf_write.addPage(pgo)

output_file = open(filename,'wb')
pdf_write.write(output_file)
output_file.close()
