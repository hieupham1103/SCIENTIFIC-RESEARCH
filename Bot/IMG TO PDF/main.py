from PIL import Image
import glob
import os

name = "The Irregular of the Royal Academy of Magic"

for x in os.listdir("./Input/"):

    url_list = glob.glob(f"./Input/{x}/*.jpg")
    image_list = []

    for i in url_list:
        # print(i)
        tempImg = Image.open(i)
        img = tempImg.convert('RGB')
        image_list.append(img)

    out = Image.open(r'./Bia.jpg')
    out = out.convert('RGB')

    out.save(f'./Output/{x}.pdf', save_all=True, append_images=image_list)
    print(x)