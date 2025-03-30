# -*- coding: cp1251 -*-
def uniq(arr_1,arr_2,arr_3):
    for i in  range (len(arr_1)):
     if arr_1[i] not in  arr_2:
        if arr_1[i] not in arr_3:
            print(arr_1[i],end=' ')


array_1 = [100, 5, 10, 20, 40, 80, 1]

array_2 = [6, 7, 20, 80, 100]

array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

#пересечения 
array_1_mn=set(array_1)
array_2_mn=set(array_2)
array_3_mn=set(array_3)

print('\t\t\tЗадача 1 \n\t\t\tРешение без множеств: ',end=' ')
for i in range (len(array_1)):
    if array_1[i] in array_2:
        if array_1[i] in array_3:
         
         print(array_1[i],end=' ')

print('\n\t\t\tРешение с множествами: ',*array_1_mn.intersection(array_2_mn,array_3_mn))
print('\n\n\n\t\t\tЗадача 2 \n\t\t\tРешение без множеств: ',end=' ')

uniq(array_1,array_2,array_3)
uniq(array_2,array_1,array_3)
uniq(array_3,array_2,array_1)
print()
# for i in  range (len(array_1)):
#     if array_1[i] not in  array_2:
#         if array_1[i] not in array_3:
         
#          print(array_1[i],end=' ')


# for i in  range (len(array_2)):
#     if array_2[i] not in  array_1:
#         if array_2[i] not in array_3:
         
#          print(array_2[i],end=' ')


# for i in  range (len(array_3)):
#     if array_3[i] not in  array_1:
#         if array_3[i] not in array_2:
         
#          print(array_3[i],end=' ')
        
print('\n\t\t\tРешение с множествами: ',*array_1_mn.difference(array_2_mn,array_3_mn)
     ,*array_2_mn.difference(array_1_mn,array_3_mn),
     *array_3_mn.difference(array_2_mn,array_1_mn))

