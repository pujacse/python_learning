# Input a positive integer (e.g. n = 153).
# Compute the sum of its digits (1+5+3 = 9).

n = 153
sum_numbers = sum(int(i) for i in str(n))
print(sum_numbers)