# coding:utf-8
import json
import re
showlist=['1 有毛发','2 能产乳','3 有羽毛','4 能飞行','5 能下蛋','6 吃肉','7 有爪子','8 有利齿','9 眼睛前视','10 有蹄子','11 黄褐色','12 深色斑点','13 深色条纹','14 长腿','15 长颈','16 白色','17 不会飞','18 黑白相杂','19 能游水','20 善于飞行' ]
print('输入特征的代号，用空格分开')
for i in showlist:
    print(i)
#print(showlist)
#print (json.dumps(showlist, encoding="UTF-8", ensure_ascii=False))
#input_list=input()
#input_list=list(x)
#input_list=input_list.split()

nums=list(map(int,input().split()))
nums.sort()

nums2=[str(i) for i in nums]
#print(nums2)
nums2.sort()
#print(nums2)

f_list=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
f_list2=list(range(1,21))
for i in nums2:
    if i not in f_list:
        print('特征 '+i+' 不在特征库里')
#rule1
if '1' in nums2:
    print('rule1:哺乳动物')
    nums2.append('A')

#rule2
if '2' in nums2:
    print('rule2:哺乳动物')
    nums2.append('A')
#rule3
if '3' in nums2:
    print('rule3:鸟类')
    nums2.append('B')
#rule4
if '4' in nums2 and '5' in nums2:
    print('rule4:鸟类')
    nums2.append('B')
#rule5
if 'A' in nums2 and '6' in nums2:
    print('rule5:食肉动物')
    nums2.append('C')
#rule6
if 'A' in nums2 and '7' in nums2 and '8' in nums2 and '9' in nums2:
    print('rule6:食肉动物')
    nums2.append('C')
#rule7
if 'A' in nums2 and '10' in nums2:
    print('rule7:有蹄动物')
    nums2.append('D')
#rule8
#rule9
if 'C' in nums2 and '11' in nums2 and '12' in nums2:
    print('rule9:它是猎豹')
    nums2.append('S1')
#rule10
if 'C' in nums2 and '11' in nums2 and '13' in nums2:
    print('rule10:它是老虎')
    nums2.append('S2')
#rule11
if 'D' in nums2 and '11' in nums2 and '12' in nums2 and '14' in nums2 and '15' in nums2:
    print('rule11:它是长颈鹿')
    nums2.append('S3')
#rule12:
if 'D' in nums2 and '12' in nums2 and '13' in nums2:
    print('rule12:它是斑马')
    nums2.append('S4')
#rule13:
if 'B' in nums2 and '17' in nums2 and '14' in nums2 and '15' in nums2 and '18' in nums2:
    print('rule13:它是鸵鸟')
    nums2.append('S5')
#rule14:
if 'B' in nums2 and '17' in nums2 and '19' in nums2 and '18' in nums2:
    print('rule14:它是企鹅')
    nums2.append('S6')
#rule15
if 'B' in nums2 and '20' in nums2:
    print('rule15:它是海燕')
    nums2.append('S7')


string1=" ".join(nums2)
#print(string1)
#print(nums2)
if (re.search('S',string1) is None):
    print('条件不足 没有这样的动物')
#for j in nums:
#    if 2 in nums:
#        nums.append('哺乳动物')
