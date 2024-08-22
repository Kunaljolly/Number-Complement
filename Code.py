class Solution:
    def findComplement(self, num: int) -> int:
        a = list(bin(num)[2:])
        for x in range(len(a)):
            if a[x] == '1':
                a[x] = '0'
            else:
                a[x] = '1'
        t = int(''.join(a),2)
        return t
