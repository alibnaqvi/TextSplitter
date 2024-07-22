# Text Splitter

This project contains a Python script that splits a large text file into smaller chunks, ensuring that no words are cut off in the middle. This can be useful for processing large documents or preparing data for tasks that require smaller text segments.

## Features

- Splits a large `.txt` file into smaller chunks based on a maximum character length.
- Ensures words are not split between chunks.
- Saves each chunk to a separate file in a specified output directory.

## Requirements

- Python 3 or above.
- `import os` with no issues.

## Usage

1. Ensure you have Python installed on your system.
2. Create a text file named `input.txt` in the same directory as the script or update the script to point to your text file.
3. Run the script to split the text file into chunks.

### Command Line

You can run the script from the command line as follows:

```sh
python text_splitter.py
```

### Example
By default, the script looks for `input.txt` in the same directory and splits the text into chunks of up to 30,000 characters. The chunks are saved in the `output_chunks` directory.

You can modify the `input.txt` file and `output_dir` variables in the script to use different input and output paths.

```
if __name__ == "__main__":
    input_file = 'path/to/your/input.txt'  # Replace with your input file path
    output_dir = 'path/to/output_directory'  # Replace with your desired output directory
    split_text_file(input_file, output_dir)
```

### Customization
You can customize the maximum length of each chunk by passing an additional parameter to the `split_text_file` function:
```
split_text_file(input_file, output_dir, max_length=50000)
```
### Contributing
If you have any problems, suggestions, or improvements, feel free to submit a pull request or open an issue.

### License
This project is licensed under the MIT License.
