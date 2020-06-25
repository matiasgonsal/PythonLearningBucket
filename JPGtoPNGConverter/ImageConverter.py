import sys
import os
from pathlib import Path
from PIL import Image


def convert_to_png(folder_from, folder_to):
    for image in os.listdir(folder_from):
        im = Image.open(folder_from + "/" + image)
        image_name, image_extension = os.path.splitext(image)
        im.save(folder_to + "/" + image_name + ".png", "PNG")


file_from = sys.argv[1]
file_to = sys.argv[2]

Path(file_to).mkdir(parents=True, exist_ok=True)

print(f"Converting Images from: {file_from}")
convert_to_png(file_from, file_to)
print(f"Process finished. Output files: {file_to}")
