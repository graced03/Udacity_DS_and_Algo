class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
 
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
    
    def to_list(self):
        target_list = []
        current_node = self.head

        while current_node is not None:
            target_list.append(current_node.value)
            current_node = current_node.next

        return target_list


def union(llist_1, llist_2):
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()

    union_set = set(list_1) | set(list_2)
    union_llist = LinkedList()
    for item in union_set:
        union_llist.append(item)
    return union_llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()

    intsec_set = set(list_1) & set(list_2)

    intsec_llist = LinkedList()
    for item in intsec_set:
        intsec_llist.append(item)
    return intsec_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1, linked_list_2))
# 32 -> 65 -> 2 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 35 -> 21 -> 
print (intersection(linked_list_1,linked_list_2))
# 4 -> 21 -> 6 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 65 -> 2 -> 3 -> 4 -> 6 -> 1 -> 8 -> 9 -> 7 -> 11 -> 35 -> 21 -> 23 -> 
print (intersection(linked_list_3,linked_list_4))
# 

# Edge Cases:
# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [2, 4, 10, 7]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# 2 -> 4 -> 10 -> 7 -> 
print(intersection(linked_list_5, linked_list_6))
#

# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_6.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
#
print(intersection(linked_list_7, linked_list_8))
#