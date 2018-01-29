from django.test import TestCase
from  .models import  usertable
# Create your tests here.
import  xlrd
data= xlrd.open_workbook('cs.xls') #打开文件
table = data.sheet_by_index(0) #获取工作表
nrows = table.nrows #行数
ncols = table.ncols #列数
colnames =  table.row_values(0)
WorkList = []
x = y = z = 0
for i in range(1,nrows):
    row = table.row_values(i) #获取每行值
    for j in range(0,ncols):
        if type(row[j]) == float: #如果值为float则转换为int,避免出现1输出为1.0的情况
            row[j] = int(row[j])
    if row: #查看行值是否为空
        if usertable.objects.filter(serv_id = row[0],user_flag=row[15]).exists():#判断该行值是否在数据库中重复
            x = x + 1 #重复值计数
        else:
            y = y + 1 #非重复计数
            WorkList.append(usertable(add_date=row[0], name=row[1], eventDetail=row[2], money=row[3], rate=row[4], note=row[5],
                                      daoxiri=row[6], phone=row[7],addres=row[8], mortgage=row[9],type=row[10],
                                      addresMortgage=row[11],
                                            )
                                    )
    else:
        z = z + 1     #空行值计数
usertable.objects.bulk_create(WorkList)
print ('数据导入成功,导入'+str(x)+'条,重复'+str(y)+'条,有'+str(z)+'行为空!')