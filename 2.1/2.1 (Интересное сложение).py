a = input()
b = input()

cl_a = list(a)
cl_b = list(b)

if len(a) > len(b):
    cl_b.append('0')
    cl_b.reverse()
elif len(a) == len(b):
    pass
else:
    cl_a.append('0')
    cl_a.reverse()

s1 = int(cl_a[0]) + int(cl_b[0])
s2 = int(cl_a[1]) + int(cl_b[1])
s3 = int(cl_a[2]) + int(cl_b[2])

g1 = str(s1)
g2 = str(s2)
g3 = str(s3)

slovo = g1[-1] + g2[-1] + g3[-1]

print(slovo)