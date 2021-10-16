# FlexTrade Systems Online Assessment
This one was hard. It was digging deep into C++ stuff.

## Q1: Stay Positive
[LeetCode 1413](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/). Minimum Value to Get Positive Step by Step Sum.

Constraints were slightly different though:
-  `1 <= n <= 10^5`
-  `-10^6 <= arr[i] <= 10^6`

**Interview Answer**:

```py
import math

def minStart(arr):
    arrSum = []
    arrSum.append(arr[0])

    for i in range(1, len(arr)):
        arrSum.append(arrSum[i-1] + arr[i])

    minSum = 1000000
    for i in range(len(arrSum)):
        if arrSum[i] < minSum:
            minSum = arrSum[i]

    if minSum == 1:
        return 0
    else:
        return 1 - minSum
    
arr1 = [-4, 3, 2, 1] # x = 5
result1 = minStart(arr1)
print(f'arr1 min start value: {result1}')

arr2 = [3, -6, 5, -2, 1] # x = 4
result2 = minStart(arr2)
print(f'arr2 min start value: {result2}')

arr3 = [5] # x = 1
result3 = minStart(arr3)
print(f'arr2 min start value: {result3}')
```

**Reflection Answer**:

The above passed all testcases but actually there was a part in the question that I totally got wrong:

> Return the minimum positive value of startValue such that the step by step sum is never less than 1.

The proper return would be:

```py
if (1 - minSum) > 1:
    return 1 - minSum
else:
    return 1
```
LeetCode answers actually gave a way shorter answer:

```py
def minStartValue(self, arr: List[int]) -> int:
    total = 0
    minSum = 0
    
    for num in arr:
        total += num
        minSum = min(minSum, total)
        
    return 1 - minSum
```

And of course we should try this in C++:

```cpp
class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int total = 0;
        int minSum = 0;
        
        for(int i = 0; i < nums.size(); ++i){
            total += nums[i];
            minSum = std::min(minSum, total);
        }
        
        return 1 - minSum;
    }
};
```


## Q2: Will the following C++ program compile?

> Will the following C++ program compile?
>
> If yes, write the statement that helps you free the entire memory allocated to p.
> 
> ```cpp
> #include <iostream>
> using namespace std;
> 
> int main()
> {
>   int* p = new int[10];
>   for ( int i = 0; i < 10; i++ )
>   {
>       p[i] = 1;
>   }
> 
>   for ( int i = 0; i < 10; i++ )
>   {
>       cout << p[i] << " ";
>   }
> 
>   // Write your statement here //
> 
>   return 0;
> }
> ```
> 
> Pick **ONE** option:
> 1. Program does not compile.
> 2. `free(p);`
> 3. `delete p;`
> 4. `delete[] p;`

**Interview Answer:**

I chose option 4. Which is [the correct one](https://www.cplusplus.com/reference/new/operator%20new[]/). `new` must match up with `delete`, and `new[]` must match up with `delete[]`.

**Reflection Answer:**

[More studying](geeksforgeeks.org/new-vs-malloc-and-free-vs-delete-in-c/) on `free()` vs `delete`:

- `free()` is a C library function that can also be used in C++, while `delete` is a C++ keyword.
- `free()` frees memory but doesn’t call Destructor of a class whereas `delete` frees the memory and also calls the Destructor of the class.

## Q3: Which is the right answer to the following?
> ```cpp
> main() {
>     struct {
>         int i;
>     }xyz;
> 
>     (*xyz)-&gt;i=10;
>     printf("%d", xyz.i);
> }
> ```
> 
> What is the output of this program? Pick **ONE** option.
> 
> 1. Compile error
> 2. 10
> 3. Garbage value
> 4. Address of i

**Interview answer:**

I chose option 1, "compile error" because `gt` appeared out of nowhere, having not been even defined let alone declared.

**Reflection answer:**

Ok, after putting this through [godbolt.org](https://godbolt.org/) with the `x86-64 gcc (trunk)` compiler, I got the following errors:

```sh
<source>:1:1: warning: ISO C++ forbids declaration of 'main' with no type [-Wreturn-type]
    1 | main() {
      | ^~~~
<source>: In function 'int main()':
<source>:6:6: error: no match for 'operator*' (operand type is 'main()::<unnamed struct>')
    6 |     (*xyz)-&gt;i=10;
      |      ^~~~
<source>:6:13: error: 'gt' was not declared in this scope
    6 |     (*xyz)-&gt;i=10;
      |             ^~
<source>:6:16: error: 'i' was not declared in this scope
    6 |     (*xyz)-&gt;i=10;
      |                ^
<source>:7:5: error: 'printf' was not declared in this scope
    7 |     printf("%d", xyz.i);
      |     ^~~~~~
<source>:1:1: note: 'printf' is defined in header '<cstdio>'; did you forget to '#include <cstdio>'?
  +++ |+#include <cstdio>
    1 | main() {
Compiler returned: 1
```

Let's break it down, pretty simple:
1. `main()` must have a return type (should have been `int main()`)
2. `xyz` is a struct, not a pointer that allows dereferencing
3. `gt` doesn't exist (where was it declared?)
4. `i` doesn't exist (people can get confused but this is not referring to `xyz.i` because again, `i` was never declared)
5. need to include `<cstdio>` to use `printf`

## Q4: What is the output of the following code?

> ```cpp
> #include 
> void main()
> {
> char letter = 'Z';
> printf("\n%c", letter);
> }
> ```
> 
> Pick **ONE** option
> 1. Z
> 2. 90
> 3. Error
> 4. Garbage value

**Interview Answer:**
I chose Z, which is totally wrong in light of Q3.

**Reflection Answer:**

1. `#include` must include something
2. `main()` must return `int`
3. `printf()` need header `<cstdio>`

## Q5: Which one of the following statements allocates enough space?

> Which one of the following statements allocates enough space to hold an array of 10 integers that > are initialized to 0?
> 
> Pick **ONE** option.
> 
> 1. ```cpp
>     int *ptr = (int *) malloc(10*sizeof(int));
>     ```
> 2. ```cpp
>     int *ptr = (int *) malloc(10, sizeof(int));
>     ```
> 3. ```cpp
>     int *ptr = (int *) calloc(10, sizeof(int));
>     ```
> 4. ```cpp
>     int *ptr = (int *) alloc(10*sizeof(int));
>     ```

**Interview Answer:**

Chose option 3. `malloc` allocates unitialized memory. There is no `alloc`.

**Reflection Answer:**

Ok, _"the *alloc variants are pretty mnemonic" - Cascabel, StackOverflow_

[Difference between malloc and calloc?](https://stackoverflow.com/questions/1538420/difference-between-malloc-and-calloc)

- malloc = memory-alloc
- calloc = clear-alloc
- realloc = re-alloc

> `calloc()` gives you a zero-initialized buffer, while `malloc()` leaves the memory uninitialized.

## Q6: Document Chunking
Could not find the LeetCode for this.

> A financial services company is uploading documents to a compliance system for analysis. They use a chunking mechanism as below.
> 
> - Each document is divided into equal sized packets.
> - Documents are then divided and uploaded in "cunks of packets. A chunk is defined as a contiguous collection of _2^n_ packets where _n_ is any interger >= 0.
> - After the document is divided into chunks. randomly selected chunks are uploaded until the entire document is completely uploaded.
> 
> There is one document that is partially uploaded, described in _uploadedChunks_. Determine the minimum number of chunks that are yet to be uploaded.
> 
> **Example**
> `totalPackets = 5`, `n = 2` number of chunks uploaded, `uploadedChunks = [[1,2]]`.
> 
> - The document has 5 packets and 1 chunk of _2^1 = 2_ packets _[1,2]_ already uploaded.
> - The remaining 3 packets are uploaded in 2 chunks. The length of _chunk1_ is _2^1 = 2_, packets _[3, 4]_, and the length of _chunk2_ is  _2^0 = 1_ packet, _[5]_.
> 
> 
> **Function Description**:
> 
> Complete the `minimumChunksRequired` function in the editor.
> 
> `minimumChunksRequired` has the following parameters:
> - `long int totalPackets`: the number of packets in the document
> - `long int uploadedChunks[n][2]`: each `uploadedChunks[i]` describes the start and end packet numbers of the uploaded chunks.
> 
> **Returns:**
> - `int`: an integer that denotes the minimum number of chunks that need to be uploaded.
> 
> **Constraints:**
> - _1 <= totalPackets < 10^18_
> - _0 <= uploaded < 10^5_
> - The uploaded chunks do not overlap
> - _1 <= starting packet <= ending packet <= totalPackets_


**Interview Answer:**
```py
def binaryPacketCountCalc(newChunkCount: int) -> int:
    count = 0
    while newChunkCount != 0:
        quotient = newChunkCount // 2
        remainder = newChunkCount % 2
        if remainder == 1:
            count += 1
            
        newChunkCount = quotient

    return count
    
    
def minimumChunksRequired(totalPackets, uploadedChunks):
    numOfChunks = len(uploadedChunks)

    chunkMap = {}

    # fill the chunk hashmap
    for chunk in uploadedChunks:
        chunkMap[chunk[0]] = chunk[1]

    chunkPtr = 1

    result = 0

    while(chunkPtr <= totalPackets):
        if chunkPtr in chunkMap:
            # skip over chunk already uploaded
            chunkPtr = chunkMap[chunkPtr]
            chunkPtr += 1
        else:
            newChunkStart = chunkPtr
            newChunkEnd = chunkPtr
            while(newChunkEnd <= totalPackets and newChunkEnd not in chunkMap):
                newChunkEnd += 1
                # when stop, newChunkEnd at end+1 of new chunk
                
            newChunkCount = newChunkEnd - newChunkStart

            result += binaryPacketCountCalc(newChunkCount)
            
            chunkPtr = newChunkEnd

    return result
    
totalPackets = 5
uploadedChunks = [[1,2]]

print(minimumChunksRequired(totalPackets, uploadedChunks))
```

This answer didn't do all test cases because of time limitation.

**Reflection Answer**:

First of all, `binaryPacketCountCalc` can totally be a litle bit more efficient.

```py
def binaryPacketCountCalc(newChunkCount: int) -> int:
    count = 0
    while newChunkCount != 0:
        remainder = newChunkCount % 2
        newChunkCount = newChunkCount // 2
        if remainder == 1:
            count += 1

    return count
```

Second, let's tackle the time limit exceed problem we currently have. It's because of this part in the code:

```py
while(newChunkEnd <= totalPackets and newChunkEnd not in chunkMap):
    newChunkEnd += 1
```

This is totally inefficient. Imagine for example we're given inputs _totalPackets = 10^5_ and _uploadedChunks = [\[10^5-1, 10^5]_ The program would have to increment to _10^5-1_ before the program can actually continue.

Trying to throw a hashmap at it was not the best idea, just use the list of uploaded chunks but sorted would have been enough.

This brings us to the full solution:

```py
def binaryPacketCountCalc(newChunkCount: int) -> int:
    count = 0
    while newChunkCount != 0:
        remainder = newChunkCount % 2
        newChunkCount = newChunkCount // 2
        if remainder == 1:
            count += 1

    return count
    
    
def minimumChunksRequired(totalPackets, uploadedChunks):
    # sort the uploadedChunks by starting packet
    uploadedChunks.sort(key= lambda chunk: chunk[0])
    
    chunkPtr = 0
    packetPtr = 1
    
    result = 0
    
    while(packetPtr <= totalPackets and chunkPtr < len(uploadedChunks)):
        if packetPtr == uploadedChunks[chunkPtr][0]:
            packetPtr = uploadedChunks[chunkPtr][1] + 1
            chunkPtr += 1
        else:
            newChunkStart = packetPtr
            newChunkEnd = uploadedChunks[chunkPtr][0]
            newChunkCount = newChunkEnd - newChunkStart
            
            result += binaryPacketCountCalc(newChunkCount)
            
            packetPtr = uploadedChunks[chunkPtr][1] + 1
            chunkPtr += 1
          
    if packetPtr < totalPackets:
        newChunkCount = totalPackets - packetPtr + 1
        result += binaryPacketCountCalc(newChunkCount)
        
    return result
    
    
totalPackets = 5
uploadedChunks = [[2,2],[1,1]]
print(minimumChunksRequired(totalPackets, uploadedChunks))

totalPackets = 5
uploadedChunks = [[5,5]]
print(minimumChunksRequired(totalPackets, uploadedChunks))
```


## Q7: Product Defects
[LeetCode 221](https://leetcode.com/problems/maximal-square/). Maximal Square.

Frikin Dynamic Programming.

## Q8: Which is the right answer to the following?

> Different compilers and host OS behaviors affect how a C program can execute. The following program was compiled with GCC and executed in a Linux host. What happens when the following program is executed?
> 
> ```cpp
> int main(void)
> {
>     char *s = "hello world";
>     *s = 'H';
> }
> ```
> 
> Pick **ONE** option:
> 
> 1. SIGABRT signal is sent
> 2. SIGSEGV signal is sent
> 3. Program runs successfully, nothing is printed
> 4. SIGILL signal is sent

**Interview Answer:**

I chose option 3. Which is gonna be the WRONG answer I think.

**Reflection Answer:**

Segmentation fault, which is SIGSEGV.

Code works on [https://www.onlinegdb.com/online_c++_compiler](https://www.onlinegdb.com/online_c++_compiler) when run, but debug shows sigsegv.

Testing on https://godbolt.org/ shows that it would be SIGSEGV.

[Reason](https://stackoverflow.com/questions/20944784/why-is-conversion-from-string-constant-to-char-valid-in-c-but-invalid-in-c), [Oracle](https://docs.oracle.com/cd/E19059-01/wrkshp50/805-4956/bajbebbg/index.html).
