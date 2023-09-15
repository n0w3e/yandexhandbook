myaso = int(input())
pr = int(input())
k1 = int(input())
k2 = int(input())

obs = myaso * pr

x = myaso * (pr - k2) / (k1 - k2)
y = myaso - x

print(round(x), round(y))