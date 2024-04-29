from PIL import Image

def text_to_binary(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

def hide_text_in_image(image_path, text_file_path, output_path):
    key = input("Enter the predetermined key: ")
    
    # Open the image and text file
    img = Image.open(image_path)
    with open(text_file_path, 'r') as file:
        text_data = file.read()

    # Convert text to binary
    binary_text = text_to_binary(text_data)

    # Ensure the image can contain the text
    if len(binary_text) > img.size[0] * img.size[1] * 3:
        raise ValueError("Text file is too large to be hidden in the image.")

    # Embed the binary text in the image using LSB and the provided key
    binary_index = 0
    pixels = list(img.getdata())

    for i in range(len(pixels)):
        pixel = list(pixels[i])
        for j in range(3):  # RGB channels
            if binary_index < len(binary_text):
                # XOR operation with Unicode code point of the key character
                pixel[j] = pixel[j] & ~1 | int(binary_text[binary_index]) ^ ord(key[binary_index % len(key)])
                binary_index += 1

        pixels[i] = tuple(pixel)

    # Create a new image with the modified pixel data
    modified_img = Image.new('RGB', img.size)
    modified_img.putdata(pixels)

    # Save the modified image
    modified_img.save(output_path)

    return output_path

# Example usage:
if __name__ == "__main__":
    image_path = input("Enter path to the image: ")
    text_file_path = input("Enter path to the text file: ")
    output_image_path = input("Enter output image path: ")

    result_image_path = hide_text_in_image(image_path, text_file_path, output_image_path)
    print("Text hidden in image:", result_image_path)
