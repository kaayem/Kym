import openpyxl


def demo():
    print("now in package")
    
    
    
TEST_PATH = "C:/Users/Kaayem/Documents/5. personal/Projects/MM set up - automation/2.GSR alignments"
file_name =TEST_PATH + '\Final - GB Amazon FACE - Wessex Final.xlsm'
wb = openpyxl.load_workbook(file_name)
type(wb)
print(wb.sheetnames)