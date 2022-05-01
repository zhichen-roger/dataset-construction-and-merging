import xlrd,xlsxwriter

url = "C:/Users/你杰哥/Desktop/python/excel"#修改为你的文件所在路径
office_file_name = "test"#修改为你使用的文件名，如前文
file_format = 'xlsx'#修改为你的数据格式
quantity = 546#修改为你的数据文件数量
allxls = []#列表
for i in range(1,quantity+1):#for循环实现多文件路径
    url_build = str(url) + "/" + str(office_file_name) + " (" + str(i) + ")." + str(file_format)
    allxls.append(url_build)
print(allxls)#先打印下看看对不对，也可删去


#目标excel
end_xls=url + "/final_excel.xlsx"#最终文件的存储路径

#函数，打开文件
def open_xls(file):
    try:
        fh=xlrd.open_workbook(file)
        return fh
    except Exception as e:
        print("打开文件错误："+e)


#根据excel名以及第几个标签信息就可以得到具体标签的内容
def get_file_value(filename,sheetnum):
    rvalue=[]
    fh=open_xls(filename)
    sheet=fh.sheets()[sheetnum]
    row_num=sheet.nrows
    for rownum in range(0,row_num):
        rvalue.append(sheet.row_values(rownum))
    return rvalue
#获取第一个excel的sheet个数以及名字作为标准
first_file_fh=open_xls(allxls[0])
first_file_sheet=first_file_fh.sheets()
first_file_sheet_num=len(first_file_sheet)
sheet_name=[]
for sheetname in first_file_sheet:
    sheet_name.append(sheetname.name)
#定义一个目标excel
endxls=xlsxwriter.Workbook(end_xls)
all_sheet_value=[]
#把所有内容都放到列表all_sheet_value中
for sheet_num in range(0,first_file_sheet_num):
    all_sheet_value.append([])
    for file_name in allxls:
        print("正在读取"+file_name+"的第"+str(sheet_num+1)+"个标签...")
        file_value=get_file_value(file_name,sheet_num)
        all_sheet_value[sheet_num].append(file_value)


num=-1
sheet_index=-1

#将列表all_sheet_value的内容写入目标excel
for sheet in all_sheet_value:
    sheet_index+=1
    end_xls_sheet=endxls.add_worksheet(sheet_name[sheet_index])
    num+=1
    num1=-1
    for sheet1 in sheet:
        for sheet2 in sheet1:
            num1+=1
            num2=-1
            for sheet3 in sheet2:
                num2+=1
                end_xls_sheet.write(num1,num2,sheet3)


endxls.close()
