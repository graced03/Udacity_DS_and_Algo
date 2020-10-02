### Problem 1
For this problem, I decided to use a OrderDict() strcture which allows me to add new element to the end of the dictionary and pop out the first element in the dictionary (which is also the least visited element) when it's full.

Using the queue structure also satifies the requirement that all operations (including get(), and set()) has a time complexity of __O(1)__, given the pop() and popitem() operations of OrderDict is __O(1)__.
The space complexity is __O(n)__ since the cache requires a max capacity of n.

### Problem 2
Here I use a recursive function to find all nested files with a desired pattern under a directory.

The time complexity if __O(n)__ given the number of iterations increases linearly as the increases in the number of total nested files under the target directory. The space complexity is directly dependent on the number of files with the desired pattern, which is __O(A)__ (assuming there are A files with the pattern under the directory).

### Problem 3
For the Huffman coding problem, I use a heap structure which helps to efficiently sort the input and create the huffman tree with a __O(nlog(n))__ time complexity. Therefore, the time complexity of encoding is __O(nlog(n))__. The time complexity of decoding is __O(n)__, where we have to traverse the encoded text to re-create the initial text input.

The space complexity of encoding and decoding is __O(n)__, which is linearly dependent on the size of the input.

### Problem 4
Here I also use a recursive function which will search into the encapsulated structure.
The time complexity depends on the number of recursive iterations, and in the worst case it would be equal to the number of subgroups of the target group. Therefore, the time complexity is essentially __O(n)__.
The space complexity is also __O(n)__ counting the stack space into account, which increases linearly as the increase in the number of groups. 

### Problem 5
The blockchain is essentially a linked list but the list is traversed backwards and has the attribute of immutability.

Similarly to linked list, the time complexity of appending is __O(1)__, searching is __O(n)__, checking the size is __O(n)__, converting to list is __O(n)__.

The space complexity if __O(n)__, which is linearly dependent on the size of the input.

### Problem 6
For this problem, I use a linked list and employ the in-build set object from python to help complete the union and intersection operation for two linked list.
Based on the spoiled code, I also maintain tail point of the linked list so that the append() function will have a complexity of __O(n)__.

In terms of time complexity, for both union and intersection, we need to convert the two linked list to a plain list first, and in the end, we also need to build a linked list based on the union and intersection list. The above operation has a time complexity of __O(n+m)__ as we have to traverse the list/linked list. 

For python set, union will take __O(n+m)__ whereas intersection will take O(min(n, m)) in the worst case. 

Therefore, in this problem, both the union and the intersection has a time complexity of __O(n+m)__.

The space complexity is __O(n+m)__ which is linearly dependent on the sizes of the two input linked list.