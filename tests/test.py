def decode(message_file):
    # Step 1: Read the file and parse the content
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    # Step 2: Extract the number and word from each line
    data = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 2:
            continue  # Skip lines that do not have exactly two parts
        number, word = parts
        data.append((int(number), word))
    
    # Step 3: Sort the data by the numbers
    data.sort()
    
    # Step 4: Identify the end-of-line numbers for each pyramid level
    pyramid_levels = []
    level = 1
    current_end = 0
    
    while current_end < len(data):
        current_end += level
        if current_end <= len(data):
            pyramid_levels.append(current_end)
        level += 1
    
    # Step 5: Extract the words corresponding to the identified numbers
    decoded_message = []
    for level_end in pyramid_levels:
        decoded_message.append(data[level_end - 1][1])
    
    # Step 6: Join the words to form the final message
    return ' '.join(decoded_message)

# Example usage
# Assuming 'message.txt' is the file containing the example input
decoded_message = decode('message.txt')
print(decoded_message)
