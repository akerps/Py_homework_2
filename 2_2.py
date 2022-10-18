# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

num = int(input("Введите число: "))
# factorial = 1
# fact_arr= [] 
# for i in range(1, num+1):
#     factorial *= i
#     fact_arr.append(factorial)

fact_num = lambda x: ((x == 1) and 1) or x * factorial(x -1)
fact_arr = list(fact_num(i) for i in range(1, num +1))

print(f'N = {num} -> {fact_arr}')
