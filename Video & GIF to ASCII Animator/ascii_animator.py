import os
import sys
import time
import cv2
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageSequence 

VIDEO_EXTENSIONS = (
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".webm",
    ".flv",
    ".wmv",
    ".mpeg",
    ".mpg",
    ".m4v",
)

GIF_EXTENSIONS = (
    ".gif",
)


def get_media_path():
    while True:
        media_path = input("Enter Media Path: ").lower()
        if not os.path.isfile(media_path):
            print("The Path Doesn't Exist.")
            continue
            
        else:
            return media_path


def load_media(media_path):

    if media_path.lower().endswith(VIDEO_EXTENSIONS):
        media = cv2.VideoCapture(media_path)

        if not media.isOpened():
            print("Couldn't open video.")
            return None

        return media

    elif media_path.lower().endswith(GIF_EXTENSIONS):
        try:
            media = Image.open(media_path)
            return media
        except Exception:
            print("Couldn't open GIF.")
            return None
    
    else:
        print("Unsupported Format.")

def get_next_frame(media):
    #Video 
    if isinstance(media, cv2.VideoCapture):
        success, frame = media.read()

        if not success:
            return None, None

        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)

            fps = media.get(cv2.CAP_PROP_FPS)

            if fps <= 0:
                fps = 30

            delay = 1 / fps

            return frame, delay
    # Gif 
    else:
        try:
            frame = media.copy()
            delay = media.info.get("duration", 100) / 1000
            media.seek = (media.tell() + 1)
            return frame, delay

        except EOFError:
            return None, None

def resize_frame(frame, new_width):
    width, height = frame.size

    index = new_width / width  # ration of widths to calculate height
    new_height = height * index * 0.55

    return frame.resize((new_width, int(new_height)))

def get_width():
    while True:
        print("\x1b[3;90mPress Enter for default.\x1b[0m")
        width_input = input("Enter Desired Width (default: 100): ")

        if not width_input:
            return 100

        try:
            width = int(width_input)

            if width < 1:
                print("Width Must Be Greater than 0.")
                continue

            return width

        except ValueError:
            print("Enter a Valid Width.")

def process_frame(frame, new_width):
    frame = frame.convert("L") #grayscaled frame
    frame = ImageOps.autocontrast(frame) #autocontrast 
    frame = ImageEnhance.Contrast(frame).enhance(2.0) #enhanced frame
    frame = frame.filter(ImageFilter.SHARPEN) #SHARPEN frame 
    frame = resize_frame(frame, new_width)

    return frame

def frame_to_ascii(frame, invert):
    ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    if invert:
        ASCII_CHARS = ASCII_CHARS[::-1]

    ascii_length = len(ASCII_CHARS) - 1
    ascii_frame = ""
    
    width, height = frame.size

    for y in range(0, height):
        for x in range(0, width):
            brightness = frame.getpixel((x,y))

            ratio = brightness / 255
            index = int(ratio * ascii_length)
            character = ASCII_CHARS[index]

            ascii_frame += character
        
        ascii_frame += "\n"

    return ascii_frame

def get_invert_choice():
    while True:
        choice = input("Invert ASCII? (y/n, default: y): ").lower()

        if not choice:
            return True

        if choice == "y":
            return True

        if choice == "n":
            return False

        print("Enter y or n.")

def display_frame(ascii_frame):
    print("\033[H\033[J", end="")
    print(ascii_frame, end="")
    sys.stdout.flush()


def play_media(media, new_width, invert):
    while True:
        frame, delay = get_next_frame(media)

        if frame is None or delay is None:
            break

        frame = process_frame(frame, new_width)
        frame = frame_to_ascii(frame, invert)
        display_frame(frame)
        
        time.sleep(delay)

def line():
    print("=================================")

def exit_cmd():
    print("\x1b[3;90mPress Ctrl+C / Ctrl+D to exit.\x1b[0m")


def main():

    line()
    print(">> VIDEO/GIF TO ASCII ANIMETOR <<")
    line()

    exit_cmd()
    
    media_path = get_media_path()
    media = load_media(media_path)

    if media is None:
        return

    new_width = get_width()
    invert = get_invert_choice()

    print("\033[2J", end="")

    play_media(media, new_width, invert)

    if isinstance(media, cv2.VideoCapture):
        media.release()

    print("\033[2J\033[H", end="")

    print("Video/GIF ended.")

if __name__ == "__main__":
    main()
