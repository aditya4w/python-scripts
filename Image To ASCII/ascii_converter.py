from PIL import Image, ImageEnhance, ImageOps, ImageFilter


def load_image():
    while True:
        try:
            image_path = input("Enter Image Path: ")

            image = Image.open(image_path)
            return image
        except FileNotFoundError:
            print("Enter a Valid Path!")

def grayscale_image(image):
    return image.convert("L")

def autocontrast_image(image):
    return ImageOps.autocontrast(image)

def enhance_contrast(image):
    return ImageEnhance.Contrast(image).enhance(2.0)

def sharpen_image(image):
    return image.filter(ImageFilter.SHARPEN)

def resize_image(image):
    width, height = image.size

    while True:
        print("\x1b[3;90mPress Enter for default.\x1b[0m")
        width_input = input("Enter Desired Width (default: 100): ")


        if not width_input:
            new_width = 100
            break

        try:
            new_width = int(width_input)

            if new_width < 1:
                print("Width Must Be Greater than 0.")
                continue

            break

        except ValueError:
            print("Enter a Valid Width.")

    index = new_width / width  # ration of widths to calculate height
    new_height = height * index * 0.55

    return image.resize((new_width, int(new_height)))
    
def ascii_image(image, invert):
    ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    if invert:
        ASCII_CHARS = ASCII_CHARS[::-1]

    ascii_length = len(ASCII_CHARS) - 1
    ascii_img = ""
    
    width, height = image.size

    for y in range(0, height):
        for x in range(0, width):
            brightness = image.getpixel((x,y))

            ratio = brightness / 255
            index = int(ratio * ascii_length)
            character = ASCII_CHARS[index]

            ascii_img += character
        
        ascii_img += "\n"

    return ascii_img

def get_invert_choice():
    while True:
        choice = input("Invert ASCII? (y/n, default: n): ").lower()

        if not choice:
            return False

        if choice == "y":
            return True

        if choice == "n":
            return False

        print("Enter y or n.")

def save_ascii(ascii_art):
    print("\nSave ASCII Art?")
    print("1. Yes")
    print("2. No")

    while True:
        try:
            choice = int(input("Choose (1 or 2): "))

            match choice:
                case 1:
                    filename = input(
                        "File name (default: output.txt): "
                    )

                    if not filename:
                        filename = "output.txt"

                    with open(filename, "w") as f:
                        f.write(ascii_art)

                    print(f"Saved as '{filename}'!")
                    return

                case 2:
                    print("Not saved.")
                    return

                case _:
                    print("Choose 1 or 2.")

        except ValueError:
            print("Enter a valid number.")

def line():
    print("==============================")

def exit_cmd():
    print("\x1b[3;90mPress Ctrl+C / Ctrl+D to exit.\x1b[0m")


def main():

    line()
    print(">> Image to ASCII Converter <<")
    line()

    exit_cmd()

    image = load_image()

    image = grayscale_image(image)
    image = autocontrast_image(image)
    image = enhance_contrast(image)
    image = resize_image(image)
    image = sharpen_image(image)

    invert = get_invert_choice()

    ascii_art = ascii_image(image, invert)

    print(ascii_art)

    save_ascii(ascii_art)
    

if __name__ == "__main__":
    main()
