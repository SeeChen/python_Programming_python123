'''
附件是一个 CSV 文件，其中每个数据前后存在空格，请对其进行清洗，要求如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬
去掉每个数据前后空格，即数据之间仅用逗号 (,) 分割；
清洗后打印输出。
示例1：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬
输入："
1, 2, 3, 4, 5
'a', 'b' , 'c' , 'd','e'
"
输出："
1,2,3,4,5
'a','b','c','d','e'
"
'''
f = open("data.csv")
s = f.read()
s = s.replace(" ","")
print(s)
