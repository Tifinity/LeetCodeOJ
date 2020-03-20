class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        # 是否是2的幂
        if num & (num -1) != 0: return False
        # 2进制0的个数是否是偶数
        if len(bin(num)[3:]) % 2 != 0: return False
        return True

    def isPowerOfFour(self, num):
        bin_str = bin(num)[2:]

        return  bin_str[0] == '1' and \
                set(bin_str[1:]).issubset({'0'}) and \
                bin_str.count('0') % 2 == 0
