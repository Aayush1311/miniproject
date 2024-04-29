from PIL import Image

def binary_to_text(binary_data):
    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        text += chr(int(byte, 2))
    return text

def extract_text_from_image(image_path, key, output_text_path):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    binary_text = ""
    key_index = 0

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            if key_index >= len(key):
                break

            bit = ord(key[key_index]) % 8
            key_index += 1

            # Extract LSB of each color channel
            r_bit = (r >> bit) & 1
            g_bit = (g >> bit) & 1
            b_bit = (b >> bit) & 1

            # Reconstruct binary text
            binary_text += str(r_bit) + str(g_bit) + str(b_bit)

    extracted_text = binary_to_text(binary_text)

    # Save extracted text to a text file
    with open(output_text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(extracted_text)

    return output_text_path

if __name__ == "__main__":
    image_path = input("Enter path to the image containing hidden text: ")
    key = input("Enter the predetermined key: ")
    output_text_path = input("Enter output text file path: ")

    extracted_text_path = extract_text_from_image(image_path, key, output_text_path)
    print("Extracted text saved to:", extracted_text_path)
