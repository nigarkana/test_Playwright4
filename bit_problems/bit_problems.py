
# 1. check even
# 2. check odd
# 3. check whether the n-th bit is 1 or 0
# 4. get 2 to the power n value
# 5. convert number to 8-bit-string 19 => "00010011"
# 6. convert 8-bit-string to a number "00010001" => 17
# 7.

def bit_is_even(n):
    return n & 1 == 0


def bit_is_odd(n):
    return n & 1 == 1


