'''
描述
大约在1500年前，《孙子算经》中就记载了这个有趣的问题。书中是这样叙述的：
今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何？
这四句话的意思是：
有若干只鸡兔同在一个笼子里，从上面数，有35个头，从下面数，有94只脚。问笼中各有多少只鸡和兔？
请编一个程序，用户在同一行内输入两个整数，代表头和脚的数量，编程计算笼中各有多少只鸡和兔，假设鸡和兔都正常，无残疾。如无解则输出Data Error!
'''
a,b = map(int,input().split(' '))
x=-b//2+2*a
y=b//2-a
if(isinstance(x,int) and isinstance(y,int) and (x>=0) and (y>=0)):
    print(x ,y)
else:
    print('Data Error!')
