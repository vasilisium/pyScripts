from appJar import gui
import xlrd
from pymongo import MongoClient
import math
#from bson import objectid


# Type symbol	Type number	    Python value
# XL_CELL_EMPTY	    0	        empty string u''
# XL_CELL_TEXT	    1	        a Unicode string
# XL_CELL_NUMBER	2	        float
# XL_CELL_DATE	    3	        float
# XL_CELL_BOOLEAN	4	        int; 1 means TRUE, 0 means FALSE
# XL_CELL_ERROR	    5	        int representing internal Excel codes; for a text representation, refer to the supplied dictionary error_text_from_code
# XL_CELL_BLANK	    6	        empty string u''. Note: this type will appear only when open_workbook(..., formatting_info=True) is used.

class xlImport:

    def __init__(self):
        self.colCount = 13  # Кол-во читаемых столбцов
        self.names = {-1: "isDeleted", 0: "rowNum", 1: "date", 2: "name", 3: "adress", 4: "wepon", 5: "calibre", 6: "weponNumber", 7: "docNumber", 8: "safeNumber", 9: "aditional"}
        #self.names = {-1: "Видалено", 0: "Номер рядку", 1: "date", 2: "name", 3: "adress", 4: "wepon", 5: "calibre",
        #              6: "weponNumber", 7: "docNumber", 8: "safeNumber", 9: "aditional"}

    def getColName(self, index):
        return self.names[index]

    def getCellValue (self, cType, cVal):
        valTmp = None
        if cType == 1:
            valTmp = cVal

        if cType == 2:
            valTmp = cVal
            numType = type(valTmp)
            div = math.modf(valTmp / 1)[0]
            if (numType is float) and (div == 0):
                valTmp = int(valTmp)

        if cType == 3:
            valTmp = xlrd.xldate.xldate_as_datetime(cVal, 0)

        if cType == 4:
            valTmp = (cVal == 1)
            if valTmp:
                tmp=None

        return valTmp


    def getRowValues(self, sheet, rowNumber):
        values = {}
        value = None

        for col in range(self.colCount):
            try:
                c = sheet.cell(rowNumber, col)
            except IndexError:
                pass
            

            if col <= 10:
                name = self.getColName(col-1)
            else:
                name = self.getColName(9)

            val = self.getCellValue(c.ctype, c.value)

            if col == 0 and (type(val) is bool):
                if not val:
                    pass
                else:
                    values[name] = val
            elif col >= 10:
                if val:
                    if not value:
                        value = ""
                    value += str(val) + " "
                if col == 12:
                    if value:
                        values[name] = value.strip()
            else:
                values[name] = val

        return values

    def export(self, xlPath):
        if filePath == '':
            return

        wb = xlrd.open_workbook(xlPath)

        client = MongoClient('localhost', 27017)
        db = client.balisticSafe

        #for sheetNumber in wb.sheets():
        for sheetNumber in range(0, 4):
            sheet = wb.sheets()[sheetNumber]
            print("Selected sheet: " + sheet.name)
            print("Rows count is: " + str(sheet.nrows))

            collection = db["ammo"]

            for r in range(2, sheet.nrows):
                v = self.getRowValues(sheet, r)
                if len(v) != 0:
                    v["collectionName"] = sheet.name
                    print(v)
                    collection.insert(v)


if __name__ == '__main__':
    app = gui()
    filePath = app.openBox(fileTypes=[('excel files', '*.xls *.xlsx')])

    xlImport = xlImport()
    xlImport.export(filePath)