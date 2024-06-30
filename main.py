from huffman import HuffmanCoding

def main():
    input_path = "input.txt"
    h = HuffmanCoding()

    compressed_path = h.compress(input_path)
    print(f"Compressed file saved as: {compressed_path}")

    decompressed_path = h.decompress(compressed_path)
    print(f"Decompressed file saved as: {decompressed_path}")

if __name__ == "__main__":
    main()
