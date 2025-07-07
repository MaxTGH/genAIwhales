import os
import random
from PIL import Image

# Replace this with the path to the folder on your computer
folder_path = r'H:\SmartWhales\TeachableMachine\Train\Whale\RealImageDataset'

# Create an output folder for cropped images
output_path = os.path.join(folder_path, 'cropped')
os.makedirs(output_path, exist_ok=True)

def resize_and_center_crop(image, size=1024):
    width, height = image.size
    scale = size / min(width, height)
    new_width = int(width * scale)
    new_height = int(height * scale)
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Calculate coordinates for center crop
    left = (new_width - size) // 2
    top = (new_height - size) // 2
    right = left + size
    bottom = top + size

    return image.crop((left, top, right, bottom))

# Collect all relevant image filenames
image_files = [
    filename for filename in os.listdir(folder_path)
    if filename.lower().endswith(('.jpg', '.jpeg', '.png'))
]

# Shuffle the order randomly
random.shuffle(image_files)

# Loop through and process shuffled images
for count, filename in enumerate(image_files):
    img_path = os.path.join(folder_path, filename)
    img = Image.open(img_path).convert('RGB')
    img_cropped = resize_and_center_crop(img)

    # Rename and save
    new_filename = f"cropped_image_{count}.jpg"
    output_img_path = os.path.join(output_path, new_filename)
    img_cropped.save(output_img_path)

print("✅ All images resized and center-cropped to 1024x1024 and saved to:", output_path)