from fixPoint import *

a = fixPoint(num=1.5, bits=32)
b = fixPoint(num=2.8, bits=32)
c = a + b
a.print()
b.print()
c.print()
print(a.bin_decimal)
print(b.bin_decimal)
print(c.bin_decimal)
d = dec_mul_dec(a.bin_decimal, b.bin_decimal)
e = a * b
print(d.bin_decimal)
e.print()
print(e.bin_decimal)
print(Bin2Dec(e.bin_decimal))