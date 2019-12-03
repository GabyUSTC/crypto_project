import math
import decimal

class fixPoint:
    def __init__(self, num, bits):
        self.bits = bits
        self.int_part = int(num)
        self.bin_decimal = Dec2Bin(num, self.bits)
        self.bin_decimal = self.bin_decimal + '0' * (self.bits - len(self.bin_decimal))
        self.decimal = Bin2Dec(self.bin_decimal)

    def print(self):
        decimal = self.decimal[2:]
        print(str(self.int_part) + '.' + decimal)

    def __add__(self, other):
        result = fixPoint(0, self.bits)
        carry = 0
        bin_decimal1 = self.bin_decimal
        bin_decimal2 = other.bin_decimal
        length = self.bits
        dec = [0] * length
        for i in reversed(range(length)):
            if int(bin_decimal1[i]) + int(bin_decimal2[i]) + carry >= 2:
                dec[i] = int(bin_decimal1[i]) + int(bin_decimal2[i]) + carry - 2
                carry = 1
            else:
                dec[i] = int(bin_decimal1[i]) + int(bin_decimal2[i]) + carry
                carry = 0
        result.int_part = self.int_part + other.int_part + carry
        result.bin_decimal = ''
        for i in dec:
            result.bin_decimal = result.bin_decimal + str(i)
        result.bits = length
        result.decimal = Bin2Dec(result.bin_decimal)
        return result

    def __mul__(self, other):
        result = fixPoint(0, self.bits)
        int1 = self.int_part
        int2 = other.int_part
        decimal1 = self.decimal
        decimal2 = other.decimal
        bin_decimal1 = self.bin_decimal
        bin_decimal2 = other.bin_decimal

        int_int = fixPoint(int1 * int2, self.bits)
        int_dec = int_mul_dec(int1, decimal2, self.bits)
        dec_int = int_mul_dec(int2, decimal1, self.bits)
        dec_dec = dec_mul_dec(bin_decimal1, bin_decimal2)

        a = int_int + int_dec
        a = a + dec_int
        return a + dec_dec

def Dec2Bin(dec, n):
    result = ''
    i = 0
    dec = dec - math.floor(dec)

    while (dec and i < n):
        dec = dec * 2
        if dec >= 1:
            result = result + '1'
        else:
            result = result + '0'
        dec = dec - math.floor(dec)
        i = i + 1
    return result

def Bin2Dec(num):
    decimal.Context().prec = 64
    result = decimal.Decimal(0)
    index = decimal.Decimal(0.5)

    for i in num:
        result = result + int(i) * index
        index = index / decimal.Decimal(2)
    result = str(result)
    if result.find("E-") != -1:
        result = result.replace('.','')
        result = '0.' + '0' * (int(result[result.find('-') + 1:]) - 1) + result[:result.find('E')]
    return result

def int_mul_dec(integer, dec, bits):
    result = fixPoint(0, bits)
    carry = 0
    dec = dec[2:]
    length = len(dec)
    output = [0] * length
    for i in reversed(range(length)):
        if int(dec[i]) * integer + carry >= 10:
            output[i] = (int(dec[i]) * integer + carry) % 10
            carry = int((int(dec[i]) * integer + carry) / 10)
        else:
            output[i] = int(dec[i]) * integer + carry
            carry = 0
    result.int_part = carry
    result.decimal = '0.'
    for i in output:
        result.decimal = result.decimal + str(i)
    result.bin_decimal = Dec2Bin(decimal.Decimal(result.decimal), bits)
    result.bin_decimal = result.bin_decimal + '0' * (result.bits - len(result.bin_decimal))
    return result

def dec_mul_dec(dec1, dec2):
    bits = len(dec1)
    length = 2 * bits
    result = fixPoint(0, bits)
    bin_dec1 = '0' * bits + dec1
    bin_dec = fixPoint(0, length)
    bin_dec.bin_decimal = bin_dec1
    bin_dec.decimal = Bin2Dec(bin_dec1)
    result_full = fixPoint(0, length)
    result_full.bin_decimal = bin_dec1
    result_full.decimal = Bin2Dec(result_full.bin_decimal)
    for i in reversed(range(bits)):
        if dec2[i] == '1':
            result_full = result_full + bin_dec
        bin_dec = int_mul_dec(2, Bin2Dec(bin_dec.bin_decimal), length)
        bin_dec.bin_decimal = bin_dec.bin_decimal + '0' * (length - len(bin_dec.bin_decimal))
    result.bin_decimal = result_full.bin_decimal[:bits]
    result.decimal = Bin2Dec(result.bin_decimal)
    return result
