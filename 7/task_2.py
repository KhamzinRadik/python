# -*- coding: cp1251 -*-


def is_prime(i_index): 
    count = 0 
    if i_index > 1: 
        for i_num in range(2, i_index // 2 + 1): 
            if (i_index % i_num) == 0: 
                count += 1 
        if count == 0: 
            return True 
        else: 
            return False 

def crypto(text): 
    return [i_sym for i_index, i_sym in enumerate(text) if is_prime(i_index)] 

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))