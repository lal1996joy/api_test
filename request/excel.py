import xlrd

wb = xlrd.open_workbook("test_ydy/test_user_data.xlsx")
sh = wb.sheet_by_name("TestUserLogin")
print(sh.nrows)
print(sh.ncols)
print(sh.cell(0, 0).value)
print(sh.row_values(0))

print(dict(zip(sh.row_values(0), sh.row_values(1))))

for i in range(sh.nrows):
    print(sh.row_values(i))
