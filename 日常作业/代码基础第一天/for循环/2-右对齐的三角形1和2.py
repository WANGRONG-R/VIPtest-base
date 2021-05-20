"""
功能描述：
编写人：
编写日期：
实现逻辑：

需求：3-右对齐的三角形1

    *   4个空格+1个*
   **   3空 + 2*
  ***   2空 + 3*
 ****   1空 + 4*
*****   0空 + 5*

分析：
    i * 数量 从1 --- 5
    空格 数量 j
    空格和*数量之和是5：i + j = 5
        j = 5 -i

"""
#
# for i in range(1,6):
#     print((5-i)* ' ' + '*' * i)


"""
需求：3-右对齐的三角形1

    
   


*****   0空 + 5*
 ****   1空 + 4*
  ***   2空 + 3*
   **   3空 + 2*
    *   4个空格+1个*

分析：
    i * 数量 从5 --- 1
    空格 数量 j
    空格和*数量之和是5：i + j = 5
        j = 5 -i


"""

for i in range(5,0,-1):
    print((5-i)* ' ' + '*' * i)