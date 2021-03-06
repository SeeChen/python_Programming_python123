'''
描述
已知列表：L=[[ 2.73351472,  0.47539713,  3.63280356,  1.4787706 ,  3.13661701],
       [ 1.40305914,  2.27134829,  2.73437132,  1.88939679,  0.0384238 ],
       [ 1.56666697, -0.40088431,  0.54893762,  3.3776724 ,  2.27490386]]
利用numpy模块，按下列要求操作，并显示相应结果。
1）写出能访问下面图片中黄色标识的数组元组的语句，将结果置于 arr1。
https://www.python123.io/images/33/2b/4d5e6f892623e60fe4343d0774e7.png
2）写出能访问下面图片中黄色标识的数组元组的语句，将结果置于 arr2。
https://www.python123.io/images/8f/d7/40362cb8eb6e26ba542316a1515f.png
3）写出能访问下面图片中黄色标识的数组元组的语句，将结果置于arr3。
https://www.python123.io/images/e9/37/2d4404902e81134b485a717599c0.png
4）找出数组中数值符合[2.5,3.5]的数据，将结果置于arr4。
5）找出数组中的负数和大于3的数，将结果置于arr5。 
'''
from numpy import *
L=[[ 2.73351472,  0.47539713,  3.63280356,  1.4787706 ,  3.13661701],
       [ 1.40305914,  2.27134829,  2.73437132,  1.88939679,  0.0384238 ],
       [ 1.56666697, -0.40088431,  0.54893762,  3.3776724 ,  2.27490386]]
arrL=array(L)
arr1=arrL[:,1:2]
arr2=arrL[1:,[2, 3, 4]]
arr3=arrL[[0, 0, 2, 2], [1, 3, 1, 3]]
arr4=arrL[(arrL >= 2.5) & (arrL <= 3.5)]
arr5=arrL[where((arrL < 0) | (arrL > 3))]
print("arr1=", arr1)
print("arr2=", arr2)
print("arr3=", arr3)
print("arr4=", arr4)
print("arr5=", arr5)
