# 10. Напишите функцию которая определит сколько раз
# встречаеться элемент в списке.
def repeat(list_, element):
    count = 0
    for i in range(0,len(list_)):
        if list_[i] == element:
            count+=1
        else:
            continue
    return count

print(repeat([3,2,46,78,9,6,7,4,67,42,4], 4))