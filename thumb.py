import glob
from PIL import Image

original_files = glob.glob("./www/img/*")
ratio = 3
print("Thumbnail process start....")
for image_file in original_files:
    print(image_file)
    original = Image.open(image_file)
    output_name = image_file[10:]
    width, height = original.size
    cropped = original.crop((0,height/2,width,height))
    cropped.thumbnail((int(width / ratio),int(height/ratio)), Image.ANTIALIAS)
    cropped.save("./www/thumb/"+output_name)
print("Thumbnail process finish....")