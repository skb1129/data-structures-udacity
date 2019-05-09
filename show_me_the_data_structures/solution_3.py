import sys
import bisect


class Node:
    def __init__(self, freq, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.data = data

    def __repr__(self):
        return "FREQ: {}, DATA: {}, LEFT: \n{}, RIGHT: \n{}".format(self.freq, self.data, self.left, self.right)

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq


def create_tree(nodes):
    while len(nodes) > 1:
        node1 = nodes.pop(0)
        node2 = nodes.pop(0)
        new_node = Node(node1.freq + node2.freq, None, node1, node2)
        bisect.insort(nodes, new_node)
    return nodes.pop()


def get_code(tree, char, code=""):
    if (not tree.left) and (char == tree.data):
        code += "0"
        return code
    if (not tree.right) and (char == tree.data):
        code += "1"
        return code
    if (not tree.right) and (not tree.right):
        return None
    code_l = code
    if tree.left is not None:
        code_l += "0"
        result = get_code(tree.left, char, code_l)
        if result is not None:
            return result
    code_r = code
    if tree.right is not None:
        code_r += "1"
        result = get_code(tree.right, char, code_r)
        if result is not None:
            return result


def huffman_encoding(data):
    frequency_map = {}
    for char in data:
        if char not in frequency_map:
            frequency_map[char] = 1
        else:
            frequency_map[char] += 1
    items = sorted(frequency_map.items(), key=lambda x: x[1])
    nodes = []
    for item in items:
        node = Node(item[1], item[0])
        nodes.append(node)
    tree = create_tree(nodes)
    encoded_data = ""
    for char in data:
        encoded_data += get_code(tree, char)
    return encoded_data, tree


def huffman_decoding(data, tree):
    node = tree
    decoded_data = ""
    for char in data:
        if node.data:
            decoded_data += node.data
            node = tree
            continue
        if char == '0':
            node = node.left
        elif char == '1':
            node = node.right
    return decoded_data


codes = {}

a_great_sentence = "The bird is the word"

print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

encoded_sentence, huff_tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_sentence, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_sentence))

decoded_sentence = huffman_decoding(encoded_sentence, huff_tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_sentence)))
print("The content of the encoded data is: {}\n".format(decoded_sentence))
