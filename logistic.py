from fixPoint import *
from matplotlib import pyplot as plt
import numpy as np
'''
a = fixPoint(num=1.5, bits=32)
b = fixPoint(num=2.8, bits=32)
c = a + b
a.print()
b.print()
c.print()
print(a.bin_decimal)
print(b.bin_decimal)
f = a - b
print(f.bin_decimal)
print(c.bin_decimal)
d = dec_mul_dec(a.bin_decimal, b.bin_decimal)
e = a * b

print(d.bin_decimal)
e.print()
print(e.bin_decimal)
print(Bin2Dec(e.bin_decimal))
'''

class logistic:
    def __init__(self, u=3.57, x0=0.5, bits=32, iters=10000):
        self.bits = bits
        self.u = fixPoint(num=u, bits=self.bits)
        self.x0 = fixPoint(num=x0, bits=self.bits)
        self.iters = iters

    def logistic_equation(self, x):
        return self.u * x * (fixPoint(num=1, bits=self.bits) - x)

    def generator(self):
        x = self.x0
        rand_seq = []
        for i in range(self.iters):
            rand_seq.append(x)
            x = self.logistic_equation(x)
        return rand_seq
'''
log1 = logistic(u=3.99, iters=300)
seq = log1.generator()
x = np.arange(0, len(seq), 1)
y = np.array([float(i.decimal) for i in seq])
print(len(x))
print(len(y))
plt.plot(x, y, 'r.')
plt.show()
'''

u_list = np.arange(3.55, 3.99, 0.01)
y = []
u_list.tolist()
for u in u_list:
    log = logistic(u=u, iters=300)
    seq = log.generator()
    y.append(float(seq[299].decimal))
plt.plot(u_list, y, 'r.')
plt.show()

