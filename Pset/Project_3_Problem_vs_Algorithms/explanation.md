## Problem 1

We want the expected time complexity to be __O(log(n))__. Therefore I implement a binary search to find the flour root of the number. For any number greater than 1, we consider the search space to be from 1 to the number itself. We divide the search space in two parts and check at each time if the squared mid_value is bigger or smaller than the given number and "shrink" the search space accordingly.

### Complexity
The time complexity is __O(log(n))__.
The space complexity is __O(1)__ given it is independent of the input.

## Problem 2
We came up with a solution based on the idea from binary search algorithm. However, given it's a rotated array, instead of simply comparing the value of the middle index element with the target value, we need to find which direction our target value goes after the rotation and then "shrink" the search space accordingly.

For this solution, the time complexity is still __O(log(n))__. This is because we only add one extra comparison in each iteration and this leads to the time complexity being __O(2log(n))=O(log(n))__.

### Complexity
The time complexity is __O(log(n))__.
The space complexity is __O(1)__ given it is independent of the input.

## Problem 3

One answer for this question is to conduct a mergesort first and we will then be able to easily construct the two numbers by using the indices given the property of the two numbers. 

### Complexity
The time complexity, which essentially the same as mergesort algorithm, is __O(log(n))__.
The space complexity is __O(n)__ which increases linearly to the number of inputs.

## Problem 4

As we learnt from the lesson 2, after we get the function to put the 0s and 2s in the correct positions, it will aotumatically cause the 1s to be in the correct positions as well.

### Complexity
The time complexity is __O(n)__ given we have to traverse the list to sort the list.
The space complexity is __O(1)__ given we only to mark the next element position for 0 and 2, and the front element index, which is independent of the input.

## Problem 5
A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
### Complexity

For Trie, time complexity of searching, inserting, testing existence from a Trie (inserting for TrieNode) depends on the length of the input word since we have to traverse each character in the word to be searched or inserted, making the runtime of these operations __O(n)__. 

Similarly, the time complexity of finding the suffixes for a given prefix in a Trie is also __O(n)__. I wrote a recursive function to find all the suffixes. The stop criteria is when the TrieNode has no children. In this case, the number of recursion needed is proportional to the length of the longest word.

For searching, inserting, testing for existence and finding all suffixes, he space complexity is __O(n)__ which increases linearly to the number of inputs.

## Problem 6

### Complexity
I perform a single transverse of the input which leads to the time complexity being __O(n)__.
The space complexity is __O(1)__ given we only need three variables, current_value, max and min, which is independent of the input.

## Problem 7

### Complexity
A RouteTrie is essentially the same as a Trie except its node has one additional handler element. 
Therefore, similar to Problem 5, the time complexity of searching and inserting from a RouterTrie (or inserting for RouterTrieNode) depends on the length of the path n, which is __O(n)__.

A Router uses RouterTrie's insert function for add a handler for a path after spliting the path into several parts, which has a time complxity of __O(n)__. Similarly, it uses RouterTrie's searching (find) function for look up spliting the path into several parts, which also has a time complxity of __O(n)__.


In term of searching and inserting from a RouterTrie, or inserting for RouterTrieNode, or look-up/add_handler in a Router, the space complexity is __O(n)__ which depends on the length of inputs. 
The worst case would be when the path (or paths)having no common folders between, requiring a node for each path block (path between forward slashes). Resulting in a space complexity of __O(n)__.
