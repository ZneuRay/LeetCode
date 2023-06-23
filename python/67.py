class Solution:
    def addBinary(self, a: str, b: str) -> str:
        arra = []
        arrb = []
        for c in a:
            arra.append(int(c))
        for c in b:
            arrb.append(int(c))
        max_len = len(arra)
        if(max_len < len(arrb)):
            max_len = len(arrb)
        sum = ''
        quotient = 0
        for i in range(max_len):
            ca = arra.pop() if arra else 0
            cb = arrb.pop() if arrb else 0
            quotient = ca + cb + quotient
            remainder = quotient % 2
            quotient = int(quotient / 2)
            sum = str(remainder) + sum
        if quotient != 0:
            sum = str(quotient) + sum
        return sum