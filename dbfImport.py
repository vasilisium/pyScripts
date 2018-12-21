from tkinter import filedialog
from tkinter import *

from dbfread  import DBF
from win32com.client import Dispatch
import os
import xlsxwriter

def export_dbf_2_xlsx(name):
    table = DBF(name)

    base = '.'.join(os.path.basename(name).split('.')[0:-1:])
    directory = os.path.dirname(filename)
    xlsFile = os.path.join(directory, base + '.xlsx')
    workbook = xlsxwriter.Workbook(xlsFile)
    worksheet = workbook.add_worksheet()

    columns_names = table.field_names
    i=0
    for column_name in columns_names:
        worksheet.write(0, i, column_name)
        i+=1

    r=1
    for record in table:
        values = list(record.values())
        c=0
        for value in values:
            a = str(value).encode('cp866').decode('cp1251')
            if a=='None':
                a=''
            worksheet.write(r, c, a) 
            c+=1
        r+=1
    workbook.close()
    return xlsFile


root = Tk()
filename =  filedialog.askopenfilename(initialdir = ".\\", \
title = "Select file", filetypes = (("dbf files","*.dbf"),))
# print(filename)
# base=os.path.basename(filename)
# print(base)
# name = base.split('.')[0]
xlFile = export_dbf_2_xlsx(filename)
xl = Dispatch("Excel.Application")
xl.Visible = True

# absPath=os.path.abspath(xlFile)
wb = xl.Workbooks.Open(xlFile)