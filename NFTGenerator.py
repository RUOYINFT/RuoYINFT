from tkinter import UNDERLINE
from PIL import Image 
import random
import os.path

RUOYI_IMG_NORMAL_NUM = 490
RUOYI_IMG_ALL_NUM = 534
RESIZE_PIX = 1000
UNDERLINE = '_'

BACKGROUND_ADDRESS_PREFIX = './background/'
RUOYI_ADDRESS_PREFIX = './human_render/'

background_type = ['Acidity', 'Cloth', 'Cyberpunk',
    'Gradual', 'Partysu', 'Smoke', 'Technology',
    'TriangularArray']
background_dict = {'Acidity':13, 'Cloth':7, 'Cyberpunk':17,
    'Gradual':8, 'Partysu':10, 'Smoke':35, 'Technology':8,
    'TriangularArray':10}

def rand_background_address():
    rand_type_num = random.randint(1, len(background_type)) - 1
    rand_type = background_type[rand_type_num]
    rand_img_num = random.randint(1, background_dict[rand_type])
    rand_background_address = BACKGROUND_ADDRESS_PREFIX + rand_type + UNDERLINE + str(rand_img_num)
    if os.path.isfile(rand_background_address + '.jpg') :
        return rand_background_address + '.jpg'
    elif os.path.isfile(rand_background_address + '.png') :
        return rand_background_address + '.png'
    else :
        print("rand_background_address: " + rand_background_address + " is wrong!")


def img_combine(image_ruoyi_address, image_background_address):
    # open img
    img_ruoyi = Image.open(image_ruoyi_address).convert('RGBA')
    img_background = Image.open(image_background_address).convert('RGBA')

    # resize background to matching RuoYi img
    background_resize_box = (50, 50, 200, 200)
    img_background_resize = img_background.resize((RESIZE_PIX, RESIZE_PIX), None, background_resize_box, reducing_gap=5.0)

    # combine RuoYi img and background img
    img_combine = Image.alpha_composite(img_background_resize, img_ruoyi).convert('RGB').save('./TestThirdWeb/test.png')


if __name__ == '__main__':
    for num in range(1,100):
        add = rand_background_address()
        print(add)