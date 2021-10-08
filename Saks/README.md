# Saks.com interview
Technical Interview with [Machine Learning Scientist](https://www.linkedin.com/in/alestainer/) at Saks.com

## First question
Instruction: Replace "!" with "." in python string. 

**Interview answer:**
Gave a for-loop answer using .append() (lol me at remembering C++)

string is immutable in python (doh me)

did mention .replace

**Reflection answer:**
The better loop would have been:

```py
input = 'Hello world!'
result = ''
for c in input:
    if c != '!':
        result += c
    else:
        result += '.'
print(result)
```

Or the python one-liner:
```py
input = 'Hello world!'
result2 = input.replace("!", ".")
print(result2)
```


## Question 2
[Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/)

**Interview Answer**:
BOMBED HARD. straight up told him I don't know and I can look it up but I rather not.


