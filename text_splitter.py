import os

def split_text_file(input_file, output_dir, max_length=30000):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as file:
        text = file.read()

    start_idx = 0
    chunks = []

    while start_idx < len(text):
        end_idx = min(start_idx + max_length, len(text))

        # Ensure we don't cut a word in half
        if end_idx < len(text) and text[end_idx] != ' ':
            last_space = text.rfind(' ', start_idx, end_idx)
            if last_space != -1:
                end_idx = last_space

        chunk = text[start_idx:end_idx]
        chunks.append(chunk.strip())

        # Move start index to the character after the current chunk
        start_idx = end_idx + 1 if end_idx < len(text) else end_idx

    # Write each chunk to a separate file
    for idx, chunk in enumerate(chunks):
        output_file = os.path.join(output_dir, f'chunk_{idx + 1}.txt')
        with open(output_file, 'w') as out_file:
            out_file.write(chunk)

    print(f'Split text into {len(chunks)} files and saved to {output_dir}')

def main():
    input_file = 'input.txt'  # Replace with your input file path
    output_dir = 'output_chunks'  # Replace with your desired output directory
    split_text_file(input_file, output_dir)
