import heapq
from collections import defaultdict

# Node in the Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

# Build the Huffman Tree
class HuffmanTree:
    def __init__(self, frequency_table):
        self.frequency_table = frequency_table
        self.root = self.build_tree()
        self.codes = {}
        self._generate_codes(self.root, "")

    def build_tree(self):
        priority_queue = [HuffmanNode(char, freq) for char, freq in self.frequency_table.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)

            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(priority_queue, merged)

        return heapq.heappop(priority_queue)

    def _generate_codes(self, node, current_code):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            return

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def get_codes(self):
        return self.codes

# Encoding the input text
class HuffmanEncoder:
    def __init__(self, codes):
        self.codes = codes

    def encode(self, text):
        encoded_text = ''.join(self.codes[char] for char in text)
        return encoded_text

# Decoding the encoded text
class HuffmanDecoder:
    def __init__(self, root):
        self.root = root

    def decode(self, encoded_text):
        decoded_text = []
        node = self.root

        for bit in encoded_text:
            node = node.left if bit == "0" else node.right

            if node.char is not None:
                decoded_text.append(node.char)
                node = self.root

        return ''.join(decoded_text)

# Compress and decompress methods
import os
import struct

class HuffmanFileCompressor:
    @staticmethod
    def compress_file(input_file, output_file):
        # Step 1: Read file content
        with open(input_file, 'rb') as file:
            content = file.read()

        # Step 2: Calculate frequencies
        frequency_table = defaultdict(int)
        for byte in content:
            frequency_table[byte] += 1

        # Step 3: Build Huffman tree
        tree = HuffmanTree(frequency_table)

        # Step 4: Encode content
        encoder = HuffmanEncoder(tree.get_codes())
        encoded_text = encoder.encode(content)

        # Step 5: Convert encoded text to bytes
        padded_encoded_text = HuffmanFileCompressor._pad_encoded_text(encoded_text)
        byte_array = HuffmanFileCompressor._convert_to_bytes(padded_encoded_text)

        # Step 6: Write compressed file
        with open(output_file, 'wb') as file:
            # Save frequency table for decompression
            file.write(struct.pack('>I', len(frequency_table)))  # Number of unique bytes
            for byte, freq in frequency_table.items():
                file.write(struct.pack('>B', byte))  # Byte
                file.write(struct.pack('>I', freq))  # Frequency

            # Write compressed content
            file.write(byte_array)

    @staticmethod
    def decompress_file(input_file, output_file):
        with open(input_file, 'rb') as file:
            # Step 1: Read frequency table
            num_entries = struct.unpack('>I', file.read(4))[0]
            frequency_table = {}
            for _ in range(num_entries):
                byte = struct.unpack('>B', file.read(1))[0]
                freq = struct.unpack('>I', file.read(4))[0]
                frequency_table[byte] = freq

            # Step 2: Rebuild Huffman tree
            tree = HuffmanTree(frequency_table)

            # Step 3: Read encoded data
            encoded_data = file.read()
            encoded_text = HuffmanFileCompressor._convert_from_bytes(encoded_data)

            # Step 4: Decode data
            decoder = HuffmanDecoder(tree.root)
            decoded_content = decoder.decode(encoded_text)

        # Step 5: Write decompressed file
        with open(output_file, 'wb') as file:
            file.write(decoded_content)

    @staticmethod
    def _pad_encoded_text(encoded_text):
        # Add padding to ensure the length is a multiple of 8
        extra_padding = 8 - len(encoded_text) % 8
        padded_info = f"{extra_padding:08b}"
        padded_encoded_text = padded_info + encoded_text + '0' * extra_padding
        return padded_encoded_text

    @staticmethod
    def _convert_to_bytes(padded_encoded_text):
        # Convert binary string to byte array
        byte_array = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            byte_array.append(int(byte, 2))
        return bytes(byte_array)

    @staticmethod
    def _convert_from_bytes(byte_data):
        # Convert byte array back to binary string
        binary_string = ''.join(f"{byte:08b}" for byte in byte_data)
        # Remove padding
        extra_padding = int(binary_string[:8], 2)
        return binary_string[8:-extra_padding]

if __name__ == "__main__":
    # Compress a file
    HuffmanFileCompressor.compress_file("input.txt", "compressed.txt")

  
    print("Compression and decompression successful!")
