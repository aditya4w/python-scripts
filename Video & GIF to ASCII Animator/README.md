## Video & GIF to ASCII Animator

Convert videos and GIFs into real-time ASCII animations directly in your terminal.

## Features

- Supports both videos and GIFs.
- Plays ASCII animation in the terminal.
- Maintains the original aspect ratio.
- Adjustable output width.
- Optional ASCII inversion.
- Automatic grayscale conversion.
- Contrast enhancement.
- Image sharpening.
- Preserves original frame rate (FPS) for videos.
- Uses each GIF frame's original duration.
- Processes one frame at a time for low memory usage.

## Requirements

- Python 3.x
- Pillow
- OpenCV

Install dependencies:

```bash
pip install pillow opencv-python
```

## Usage

Run the script:

```bash
python ascii_animator.py
```

The program will ask for:

- Media file path
- Output width
- Whether to invert the ASCII characters

## Example

An example video named **`no.mp4`** is included in this repository for testing.

Simply enter its path when prompted, for example:

```text
no.mp4
```

## How it Works

1. Loads the media file.
2. Reads one frame at a time.
3. Converts the frame to grayscale.
4. Applies automatic contrast enhancement.
5. Sharpens the frame.
6. Resizes while preserving the aspect ratio.
7. Maps pixel brightness to ASCII characters.
8. Displays the ASCII frame in the terminal.
9. Repeats until playback finishes.

## Project Structure

```
ascii_animator.py
README.md
no.mp4
```

## Notes

- Videos are played using their original FPS.
- GIFs use the duration stored in each frame.
- Frames are streamed one at a time instead of loading the entire file into memory, making playback more memory-efficient.

## License

This project is open source and part of my *python-scripts.*
