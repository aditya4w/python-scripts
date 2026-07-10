# Image to ASCII

A command-line tool that converts images into ASCII art directly in the terminal.

## Features

- Convert images to grayscale
- Automatic contrast enhancement
- Image sharpening
- Preserve image aspect ratio while resizing
- Custom output width
- Optional ASCII inversion
- Save ASCII art to a `.txt` file
- Input validation and error handling

## Requirements

- Python 3.10+
- Pillow

Install Pillow:

```bash
pip install pillow
```

## Usage

Run the script:

```bash
python ascii_converter.py
```

The program will:

1. Ask for an image path.
2. Ask for the output width (press Enter for the default).
3. Ask whether to invert the ASCII characters.
4. Display the generated ASCII art.
5. Optionally save the output as a `.txt` file.

## Example

```text
Image Path: image.jpg
Width: 100
Invert ASCII? (y/n): n
```


The generated ASCII art is displayed in the terminal and can be saved as a text file.

## Built With

- Python
- Pillow (PIL)

## License

This project is part of my **Python Scripts** collection.
