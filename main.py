import zipfile
from docxtpl import DocxTemplate
from docx2pdf import convert
import codecs
Date1 = 15.021
Date2 = 22.013
Olympiad = "Городская олимпиада по математике"

z = zipfile.ZipFile('zipfile.zip', 'w')
f = codecs.open('Data.txt', 'r', "utf_8_sig")

for name in f:
    doc1 = DocxTemplate("test.docx")
    context1 = {'Name': name.rstrip(), 'Olympiad': Olympiad, 'Date1': Date1, 'Date2': Date2}
    doc1.render(context1)
    doc1.save("{}_olympiad.docx".format(name.rstrip()))
    convert("{}_olympiad.docx".format(name.rstrip()))
    z.write("{}_olympiad.pdf".format(name.rstrip()))
f.close()
z.close()