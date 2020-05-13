#       Catalog.py
#       spreadsheet file writing

from os import path
import xlrd
import xlsxwriter


def write(herb):
    h = [herb.name, herb.origin, herb.rarity, herb.color, herb.type, herb.use, herb.delivery, herb.expiration]

    if path.exists('Herbs.xlsx'):
        # print('Herbs.xlsx already exists.')
        wbexists = xlrd.open_workbook('Herbs.xlsx')         # Opens existing Worksheet
        sheets = wbexists.sheets()                          # saves old sheets into iterable list
        workbook = xlsxwriter.Workbook('Herbs.xlsx')        # creates new list
        for sheet in sheets:                                    # parse thru old sheets,
            worksheet = workbook.add_worksheet(sheet.name)       # writing them to a newsheet
            for row in range(sheet.nrows):                          # we do this to get last clean row
                if row == 0:                # in the header row
                    headerformat = workbook.add_format({'bold': True, 'font_name': 'Segoe UI Semibold', 'font_size': 15,
                         'bg_color': '#00c462', 'bottom': 1, 'border_color': 'black'})        # define header format, consistent with creation
                    for col in range(sheet.ncols):
                        worksheet.write(row, col, sheet.cell(row, col).value, headerformat)  # write and add formatting
                else:
                    for col in range(sheet.ncols):
                        worksheet.write(row, col, sheet.cell(row, col).value)
                    lastrow = row + 1               # save the last iterated row value, move to next
        col = 0                                 # restart the columns
        for _ in h:                             # write new exported herbs
            worksheet.write(lastrow, col, h[col])        # to an empty row at the end of the spreadsheet
            col += 1

    else:
        #SPREADSHEET DOES NOT EXIST.
        #DEFINE HEADER ROW
        header = ['Herb Name', 'Origin', 'Rarity', 'Color', 'Texture', 'Use', 'Delivery', 'Expiration']     # header cell values
        workbook = xlsxwriter.Workbook('Herbs.xlsx')        # creates workbook obj
        headerformat = workbook.add_format({'bold': True, 'font_name': 'Segoe UI Semibold', 'font_size': 15, 'bg_color': '#00c462', 'bottom': 1})
        worksheet = workbook.add_worksheet('Herbs.xlsx')
        worksheet.write_row(0, 0, header, headerformat)       # fill row 1, starting at column 1, with Header values
        worksheet.write_row(1, 0, h)            # write row 2, starting at column 1, with herb values

    worksheet.set_row(0, 40)  # set row 1 height to 40
    worksheet.set_column('A:A', 30)  # set name column width to 2.0
    worksheet.set_column('B:B', 20)  # origin column
    worksheet.set_column('C:C', 10)  # rarity
    worksheet.set_column('D:H', 15)  # color, texture, use, deliver, expiration
    worksheet.autofilter('A1:D11')   # filter functionality in the headers for easy sorting

    # todo: implement parser to each herb row with specific background colors

    workbook.close()        # save the data
    print(herb.name + ' exported to %s' % path.abspath('Herbs.xlsx'))       # log checker

