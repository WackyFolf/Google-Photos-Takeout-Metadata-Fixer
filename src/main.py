from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime
import json, glob

images = glob.glob('*.jpg') # Create list with all JPEGs in folder (I'll add PNGs later)

for x in range((len(images))-1):
    activeImage = images[x]
    try:
        with open(activeImage, 'rb') as image_file:
            image = Image(image_file) # Open image to edit
        with open(activeImage + '.json', 'r') as image_data: # Open corresponding JSON file
            imageData = json.load(image_data)
            timetaken = int(imageData["photoTakenTime"]["timestamp"]) # Find timestamp in JSON file
        image.datetime_original = datetime.utcfromtimestamp(timetaken).strftime(DATETIME_STR_FORMAT) # Add date to image, formatted how it likes it
        with open(activeImage, 'wb') as new_image_file: # Open image for writing
            new_image_file.write(image.get_file()) # Save file
        print("Processed " + activeImage)
    except Exception as e:
        if "[Errno 2] No such file or directory" in str(e):
            e = "Could not find corresponding JSON."
        print("Failed to process " + activeImage + ". " + str(e)) # Bare-bones error thingy





