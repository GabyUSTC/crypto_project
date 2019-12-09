from fixPoint import *
from matplotlib import pyplot as plt
import numpy as np
import time
import decimal
from multiprocessing import Pool
'''
a = fixPoint(num=1.6, bits=32)
b = fixPoint(num=2.8, bits=32)
c = a + b
a.print()
b.print()
c.print()
print(a.bin_decimal)
print(b.bin_decimal)
print(c.bin_decimal)
f = a - b
print(f.bin_decimal)
e = a * b
e.print()
print(e.bin_decimal)
'''
def period_test(u, bits=32):
    x0_list = np.arange(0.1, 0.9, 0.1)
    x0_list.tolist()
    count = 0
    for x0 in x0_list:
        seq = []
        log = logistic(u=u, x0=x0, bits=bits)
        x = log.x0
        while x.decimal not in seq:
            seq.append(x.decimal)
            x = log.logistic_equation(x)
            count += 1
        #count = count - seq.index(x.decimal)
    print(u, count / len(x0_list))
    return count / len(x0_list)

class logistic:
    def __init__(self, u=3.57, x0=0.5, bits=32, iters=10000):
        self.bits = bits
        self.u = fixPoint(num=u, bits=self.bits)
        self.x0 = fixPoint(num=x0, bits=self.bits)
        self.iters = iters

    def logistic_equation(self, x):
        return self.u * x * (fixPoint(num=1.0, bits=self.bits) - x)

    def generator(self):
        x = self.x0
        rand_seq = []
        for i in range(self.iters):
            rand_seq.append(x)
            x = self.logistic_equation(x)
        return rand_seq

    def file_output(self):
        seq = self.generator()
        context = '#==================================================================\n' \
                  '# generator logistic  seed = {0}{1}\n' \
                  '#==================================================================\n'\
                  'type: d\n' \
                  'count: {2}\n' \
                  'numbit: {3}\n'.format(self.u.int_part, self.u.decimal[1:], self.iters, self.bits)
        for rand in seq:
            rand = int('0b' + rand.bin_decimal, 2)
            context = context + str(rand) + '\n'
            #context = context + str(rand.int_part) + rand.decimal[1:] + '\n'
            #context = context + rand.bin_decimal + '\n'
        f = open("random.txt", mode="w", encoding="utf-8")
        f.write(context)
        f.close()
'''
start = time.time()
period_test(3.9989)
log1 = logistic(u=3.9989, iters=800, x0=0.5)
seq = log1.generator()
x = np.arange(0, len(seq), 1)
y = np.array([int('0b' + i.bin_decimal, 2) for i in seq])
end = time.time()
print('Running time: %s Seconds'%(end-start))
plt.plot(x, y, 'r.')
plt.show()
'''




'''
u_list = np.arange(3.56, 4, 0.01)
x0_list = np.arange(0.1, 0.9, 0.1)
T = []
u_list.tolist()
x0_list.tolist()
start = time.clock()
for u in u_list:
    count = 0
    for x0 in x0_list:
        seq = []
        log = logistic(u=u, x0=x0, bits=8, iters=100)
        x = log.x0
        while x.decimal not in seq:
            seq.append(x.decimal)
            x = log.logistic_equation(x)
            count += 1
    T.append(count / len(x0_list))
end = time.clock()
print(u_list)
print(T)
print('Running time: %s Seconds'%(end-start))
plt.plot(u_list, T, 'r')
plt.show()
'''
'''
u_list = np.arange(3.56, 4, 0.01)
u_list.tolist()
start = time.time()
pool = Pool()
T = pool.map(period_test, u_list)
pool.close()
pool.join()
end = time.time()
print('Running time: %s Seconds'%(end-start))
print(T)
plt.plot(u_list, T, 'r')
plt.show()
'''

start = time.time()
log1 = logistic(u=3.9989, iters=40000, bits=32, x0=0.5)
log1.file_output()
end = time.time()
print('Running time: %s Seconds'%(end-start))
