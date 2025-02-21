import cv2
import os
import string

# Load the image
img_path = "Passport_Photograph.jpeg"
img = cv2.imread(img_path)

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Unable to open image file at {img_path}. Please check the file path.")
    exit()

# Get secret message and password from user
msg = input("Enter secret message: ")
password = input("Enter password: ")

# Create dictionaries for character encoding and decoding
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Initialize coordinates for pixel manipulation
n, m, z = 0, 0, 0

# Encode the message into the image
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3
    if n >= img.shape[0]:  # Move to the next row if we reach the end of the current row
        n = 0
        m += 1
    if m >= img.shape[1]:  # Stop if we exceed the image dimensions
        print("Warning: Message is too long to fit in the image.")
        break

# Save the modified image
cv2.imwrite("Encryptedmsg.jpg", img)
os.system("start Encryptedmsg.jpg")

# Decrypt the message
message = ""
n, m, z = 0, 0, 0

# Get password for decryption
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for _ in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
        if n >= img.shape[0]:  # Move to the next row if we reach the end of the current row
            n = 0
            m += 1
        if m >= img.shape[1]:  # Stop if we exceed the image dimensions
            break
    print("Decrypted message: ", message)
else:
    print("Not valid key!!!!")