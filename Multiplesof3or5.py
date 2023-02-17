## If we list all the natural numbers below 10 that are multiples of 3 or 5,
## we get 3, 5, 6 and 9. The sum of these multiples is 23.
## Find the sum of all the multiples of 3 or 5 below 1000.
summ = 0
a = 1
while a < 1000:
    if a % 3 == 0 or a % 5 == 0:
        summ = summ + a
    a += 1
print(summ)
