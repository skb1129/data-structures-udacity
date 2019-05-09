class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

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
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def get_list_data(self):
        cur_head = self.head
        data = []
        while cur_head:
            data.append(cur_head.value)
            cur_head = cur_head.next
        return data


def union(llist_1, llist_2):
    l1 = llist_1.get_list_data()
    l2 = llist_2.get_list_data()
    ll = []
    linked_list = LinkedList()
    for value in l1:
        if value not in ll:
            ll.append(value)
            linked_list.append(value)
    for value in l2:
        if value not in ll:
            ll.append(value)
            linked_list.append(value)
    return linked_list


def intersection(llist_1, llist_2):
    l1 = llist_1.get_list_data()
    l2 = llist_2.get_list_data()
    ll = []
    linked_list = LinkedList()
    for value in l1:
        if (value in l2) and (value not in ll):
            ll.append(value)
            linked_list.append(value)
    for value in l2:
        if value not in ll:
            ll.append(value)
            linked_list.append(value)
    return linked_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [10, 29, 12, 1, 2, 4, 8, 2]
element_2 = [5, 7, 2, 9, 4, 7, 2]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))
