from appJar import gui
import xlrd
import getopt

colCount = 13  # Кол-во читаемых столбцов


def getRowValues(sheet, rowNumber):
    values = {}
    name = {-1: "isDeleted", 0: "rowNum", 1: "date", 2: "name", 3: "adress",
            4: "wepon", 5: "calibre", 6: "weponNumber", 7: "docNumber",
            8: "safeNumber", 9: "aditional"}
    for col in range(colCount):
        c = sheet.cell(rowNumber, col)

        if c.ctype not in [0, 6]:
            if c.ctype == 3:
                values[name[col-1]] = xlrd.xldate.xldate_as_datetime(c.value, 0)
            else:
                values[name[col-1]] = c.value

            if col > 10:
                values[name[9]] += " " + c.value
    return values


def export(filePath):
    if filePath == '':
        return

    from pymongo import MongoClient

    wb = xlrd.open_workbook(filePath, formatting_info=True)

    mongo = MongoClient('localhost', 27017)
    db = mongo.balisticSafe

    #for sheet in wb.sheets():
    sheet = wb.sheets()[0]
    print("Selected sheet: " + sheet.name)
    print("Rows count is: " + str(sheet.nrows))

    collection = db[sheet.name]
    for r in range(2, sheet.nrows):
        v = getRowValues(sheet, r)
        if len(v) != 0:
            print(v)
            collection.insert(v)


app = gui()
filePath = app.openBox(fileTypes=[('excel files', '*.xls *.xlsx')])

export(filePath)
