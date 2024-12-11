# author zyy
# time 2024/12/10 15:05
import openpyxl


def read_excel(x):
    res_data=[]
    workbook=openpyxl.load_workbook(x)
    sheet=workbook["Sheet1"]
    keys=[key.value for key in sheet[2]]
    for values in sheet.iter_rows(min_row=3,values_only=True):
        d=dict(zip(keys,values))
        if d["is_true"]:
            res_data.append(d)
    workbook.close()
    return res_data