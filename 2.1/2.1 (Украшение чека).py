a = input()
b = int(input())
c = int(input())
d = int(input())

cena = f'{c}кг * {b}руб/кг'
summa = f'{c*b}'
hm = f'{d}'
cda = f'{d-(c*b)}'

n1 = len('продукт')
n2 = len('числo')

print("================Чек================")
print(f'Товар: {a.rjust(35 - n1)}')
print(f"Цена:{cena.rjust(35 - n2)}")
print(f"Итого:{summa.rjust(35 - 9)}руб")
print(f"Внесено:{hm.rjust(35 - 11)}руб")
print(f"Сдача:{cda.rjust(35 - 9)}руб")
print('===================================')

