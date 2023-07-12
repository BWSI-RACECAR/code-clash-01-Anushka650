def isPalindrome(self, x):
    if x < 0:
        return False
    rev_x = 0
    temp = x
    while temp != 0:
        curr = temp % 10
        rev_x = rev_x * 10 + curr
        temp = temp // 10
    if rev_x == x:
        return True
    else:
        return False
