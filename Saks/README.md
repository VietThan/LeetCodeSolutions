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

**Reflection answer:**

```py
class SparseVector:
    def __init__(self, nums: List[int]):
        self.noZero = {}
        for i, val in enumerate(nums):
            if val != 0:
                self.noZero[i] = val

    def dotProduct(self, vec: 'SparseVector'):
        if len(vec.noZero) < len(self.noZero):
            return vec.dotProduct(self)

        result = 0
        for i, val in self.noZero.items():
            if i in vec.noZero:
                result += vec.noZero[i] * val

        return result

nums1 = [0,0,0,0,0,7,1]
nums2 = [0,0,0,0,0,0,1]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)

print(ans)
```


Learnt a bunch, like:

```py
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
```

But alright, I'm gonna get good.

The guy was encouraging, in his own Russian way. Let's go through the Python tutorial.