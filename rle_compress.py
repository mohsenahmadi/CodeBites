#Given a byte array, write code to compress it using run-length encoding (RLE). For each 
# consecutive sequence of identical values in the input array, count the occurrences and output the 
# count followed by the value. The output will be a list with alternating count-value pairs 
# representing the compressed data.

# Input byte array
byte_array = [170, 170, 170, 187, 187, 187, 187, 187, 204, 11, 11, 55, 55, 170, 170]

# Run-length encoding
compressed = []
i = 0
while i < len(byte_array):
    count = 1
    while i + 1 < len(byte_array) and byte_array[i] == byte_array[i + 1]:
        count += 1
        i += 1
    compressed.extend([count, byte_array[i]])
    i += 1

# Output the compressed byte array
print(compressed)