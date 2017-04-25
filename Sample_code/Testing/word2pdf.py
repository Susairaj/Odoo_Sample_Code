# import sys
# import os
# import comtypes.client
# 
# wdFormatPDF = 17
# 
# in_file = '/home/susai/Documents/Python_test/Odoo Installation(Ubuntu).docx'
# out_file = '/home/susai/Documents/Python_test'
# 
# word = comtypes.client.CreateObject('Word.Application')
# doc = word.Documents.Open(in_file)
# doc.SaveAs(out_file, FileFormat=wdFormatPDF)
# doc.Close()
# word.Quit()

from subprocess import Popen, PIPE
import time

def convert(src, dst):
    d = {'src': src, 'dst': dst}
    commands = [
        '/usr/bin/docsplit pdfimages --output %(dst)s %(src)s' % d,
        'oowriter --headless -convert-to pdf:writer_pdf_Export %(dst)s %(src)s' % d,
    ]

    for i in range(len(commands)):
        command = commands[i]
        st = time.time()
        process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True) # I am aware of consequences of using `shell=True` 
        out, err = process.communicate()
        errcode = process.returncode
        if errcode != 0:
            raise Exception(err)
        en = time.time() - st
        print 'Command %s: Completed in %s seconds' % (str(i+1), str(round(en, 2)))

if __name__ == '__main__':
    src = '/home/susai/Documents/Python_test/Odoo Installation.docx'
    dst = '/home/susai/Documents/Python_test'
    convert(src, dst)
    
    
    
    
    