# Simulate rolling a die 5 times and take guesses for the outcomes
# Print the ratio of successes to failures,
# but watch out for division by 0 --------------------------------------------------------------
# Pseudocode
# --------------------------------------------------------------
random.seed(19)
# 0. initialize the guesses, say to 6, 1, 5, 1, 5        #19
guesses = [6, 1, 5, 1, 5]
# 1. initialize countright and countwrong
countright = countwrong = 0
# 2. loop 5 times
for i in range(5) :
    # 3. roll die
    roll = random.randint(1, 6)
    # 4. ask for guess
    guess = guesses[i]
    # 5. change countright or countwrong
    if roll == guess :
        countright = countright + 1
    else :
        countwrong = countwrong + 1
# 6. try block to
try :
    # 7. evaluate the ratio
    ratio = countright / countwrong
    # 8. print the ratio
    print('countright, countwrong, ratio = ', countright, countwrong, ratio)
    # 9. print done try
    print('done try block')
# 10. except if there is a zero division error
except ZeroDivisionError :
    # 11. print no failures, so no ratio
    print('no failures, so no ratio')
    # 12. print done except
    print('done the except block')