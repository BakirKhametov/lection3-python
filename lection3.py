# def f(x):
#  return x**2
# print(f(4))

# q = f

# print (f(4))   
# print(q(4)) # Функция def f(x) может быть приравнена к какой-нибудь переменной (q) (q = f) 
# и при вызове работать как фунция

# def calc1(x):
#     return x+10

# def calc2(x):
#     return x*10

# def math(op, x):
#     print(op(x))

# math (calc1, 10)
# math (calc2, 10)   # В качесте аргумента была передана функция calc1 и calc2, а в качестве х цифра 10
# Результат math (calc1, 10) = 20 (х(10) + 10) - функция calc1
# Результат math (calc2, 10) = 100 (х(10) * 10) - функция calc2

# def sum(x, y):
#     return x+y

# f = lambda x, y: x+y # def sum(x, y):return x+y и f = lambda x, y: x+y - функции с одинаковой логикой,
#просто записанные по разному



# def mult(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
    #return op(a, b)

# calc(mult, 4, 5)  # Результат calc(mult, 4, 5) = 20, 
# так как функция mult возвращает произведение аргументов 4 и 5 (def mult(x, y):return x*y)
# calc(f, 4, 5) # Результат calc(f, 4, 5) = 9 так как функция f возвращает сумму аргументов 4 и 5 (f = lambda x, y: x+y)
# calc(lambda x, y: x+y, 4, 5) # упрощенная форма записи

# list = []
# for i in range(1, 21):
#     if(i%2 == 0):
#         list.append(i)
# print(list)

# list = [i for i in range(1, 21) if i%2 == 0]
# print(list)
# Два варианта записи списка: обычный и упрощенный

# list = [(i, i) for i in range(1, 21) if i%2 == 0]
# print(list)
 # Вариант записи кортежа

# def f(x):
#   return x**3
# list = [f(i) for i in range(1, 21) if i%2 == 0]
# print(list)
# Из списка с 1 по 21 число выбрали все четные а потом возвели в степень 3 при помощи функции def f(x):return x**3
# [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]
# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list)
# Запись кортежа четное число из промежутка от 1 до 21 и его значение в кубе
# [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]


# def select(f, col):
#     return[f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res) # Результат: [(2, 4), (8, 64), (38, 1444)]

# li = [x for x in range(1, 20)]
# print(li)
# li = list(map(lambda x:x+10, li))
# print(li) # Результат: список от 1 до 19 включительно 
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# был преобразован путем прибавления к каждому элементу цифры 10
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# data = list(map(int, input().split()))
# print(data) # Ввод 1 2 3 4 5 6 7 8 9 , вывод [1, 2, 3, 4, 5, 6, 7, 8, 9]

# !(def select(f, col):
#     ! return[f(x) for x in col]
#! def where(f, col):
#  !   return [x for x in col if f(x)]) Часть которую заменили функцииlambda, map, filter
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res) # Работа предыдущей функции только через lambda, map, filter , результат тот же [(2, 4), (8, 64), (38, 1444)]

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # Результат:[('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# первый элемент users был совмещен с первым элементом ids и так далее.

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # Результат: [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# users = ['user1','user2','user3','user4','user5']
# data = list(enumerate(users))
# print(data) # Результат: [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]
# функция enumerate выводит индексы элементов потом сами элементы








