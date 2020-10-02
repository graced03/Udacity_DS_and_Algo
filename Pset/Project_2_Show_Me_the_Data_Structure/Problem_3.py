import heapq
import sys

class Node:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self, other):
		
		if(other == None):
			return -1
		if(not isinstance(other, Node)):
			return -1
		return self.freq < other.freq

class HuffmanEncoder:
    def __init__(self, data):
        self.data = data
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
        self.frequency = {}

    def make_frequency_dict(self):
        for character in self.data:
            if not character in self.frequency:
                self.frequency[character] = 0
            self.frequency[character] += 1
    
    def create_heap(self):
        for key in self.frequency:
            heapq.heappush(self.heap, Node(key, self.frequency[key]))

    def merge_nodes(self):
        while(len(self.heap)>1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def _create_codes_recursive(self, root, current_code):
        if(root == None):
            return
        if(root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self._create_codes_recursive(root.left, current_code + "0")
        self._create_codes_recursive(root.right, current_code + "1")

    def create_codes(self):
        self.make_frequency_dict()
#         print(self.frequency)
        self.create_heap()
        self.merge_nodes()
        
        root = heapq.heappop(self.heap)
        
#       assign "0" as the code for sentences with single character
        if (root.left is None) and (root.right is None):
            self.codes[root.char] = "0"
            self.reverse_mapping["0"] = root.char
        else:
            init_code = ""
            self._create_codes_recursive(root, current_code = init_code)
        
#         print(self.codes)
#         print(self.reverse_mapping)
    
    def get_encoded_text(self):
        self.create_codes()
        encoded_text = ""
        for character in self.data:
            encoded_text += self.codes[character]
        return encoded_text
    
    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if(current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

def huffman_encoding(data):
    if len(data) == 0:
        print("String is null!")
        return

    encoder = HuffmanEncoder(data)
    encoded_text = encoder.get_encoded_text()
    return encoded_text, encoder
    

def huffman_decoding(encoded_data, encoder):

    return encoder.decode_text(encoded_text)

# Testing
if __name__ == "__main__":
    
    # Testing 1	
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
	# The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
	# The content of the data is: The bird is the word

    encoded_text, encoder = huffman_encoding(data = a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_text, base=2))))
	# The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_text))
	# The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001


    decoded_text = huffman_decoding(encoded_text, encoder)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_text)))
	# The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_text))
	# The content of the encoded data is: The bird is the word

    # Testing 2

    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
	# The size of the data is: 74
    print ("The content of the data is: {}\n".format(a_great_sentence))
	# The content of the data is: AAAAAAABBBCCCCCCCDDEEEEEE

    encoded_text, encoder = huffman_encoding(data = a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_text, base=2))))
	# The content of the encoded data is: 1010101010101000100100111111111111111000000010101010101
    print ("The content of the encoded data is: {}\n".format(encoded_text))
	# The size of the decoded data is: 74

    decoded_text = huffman_decoding(encoded_text, encoder)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_text)))
    print ("The content of the encoded data is: {}\n".format(decoded_text))
	# The size of the decoded data is: 74
	# The content of the encoded data is: AAAAAAABBBCCCCCCCDDEEEEEE

    # Tesing 3 - Edge case
    a_great_sentence = "AAAA"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
	# The size of the data is: 53
	# The content of the data is: AAAA

    encoded_text, encoder = huffman_encoding(data = a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_text, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_text))
	# The size of the encoded data is: 24
	# The content of the encoded data is: 0000

    decoded_text = huffman_decoding(encoded_text, encoder)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_text)))
    print ("The content of the encoded data is: {}\n".format(decoded_text))
	# The size of the decoded data is: 53
	# The content of the encoded data is: AAAA

    # Tesing 4 - Edge case
    a_great_sentence = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
	# The size of the data is: 49
	# The content of the data is: 

    encoded_text, encoder = huffman_encoding(data = a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_text, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_text))

	# String is null!
	# TypeError: cannot unpack non-iterable NoneType object
	# (This case the string is null so that we has a TypeError)


