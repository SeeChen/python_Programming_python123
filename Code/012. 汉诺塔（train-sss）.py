'''
描述
汉诺塔：汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
柱子编号为a, b, c，将所有圆盘从a移到c可以描述为： 
如果a只有一个圆盘，可以直接移动到c； 
如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。 
请编写一个函数move(n, a, b, c) ，给定输入 n, a, b, c，打印出移动的步骤： 
例如，输入 move(2, ‘A’, ‘B’, ‘C’)，打印出： 
A –> B
A –> C
B –> C
输入格式
有两行：
第一行一个正整数
第二行有三个符号，如A、B、C或a,b,c等，输入时用空格分隔开。
输出格式
移动过程的记录 
'''
def hanoi_move(n, a, b, c):
	if n == 1:
		print(a, '-->', c)
		return None
	else:
		hanoi_move(n - 1, a, c, b)
		hanoi_move(1, a, b, c)
		hanoi_move(n - 1, b, a, c)
if __name__ == '__main__':
	num = int(input())
	s1, s2, s3 = input().split()
	hanoi_move(num, s1, s2, s3)
