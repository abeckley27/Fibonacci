def nth_fib(n):
    #Return the nth fibonacci number
    a = 1
    b = 0
    for j in range(n - 2):
        a += b
        b = a - b
    return a + b


def fib_seq(n):
    #Return the first n terms of the fibonacci sequence
    a = 1
    b = 0
    output = [1]
    for j in range(n - 1):
        a += b
        b = a - b
        output.append(a)
    return output

def fib_sum(n):
    #Return the nth partial sum of the fibonacci sequence
    a = 1
    b = 0
    output = 1
    for j in range(n - 1):
        a += b
        b = a - b
        output += a
    return output


#Project Euler problem 2
x = fib_seq(40)
answer = 0
for k in x:
    if k <= 4000000:
        answer += k
    else:
        break

print(answer)
