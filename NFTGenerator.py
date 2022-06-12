import re
from time import sleep
from tkinter import UNDERLINE
from unittest import case
from PIL import Image 
import random
import os.path
import json

RUOYI_IMG_NORMAL_NUM = 490
RUOYI_IMG_ALL_NUM = 534
RUOYI_ALL_NUM = 1024
RESIZE_PIX = 1000
UNDERLINE = '_'

BACKGROUND_ADDRESS_PREFIX = './background/'
RUOYI_ADDRESS_PREFIX = './human_render/ruoyi_'
COMBINE_ADDRESS_PREFIX = './NFTUltimately/'

JSON_ADDRESS = './RuoYi.json'
JSON_NAME = 'RuoYi #'
JSON_DESCRIPTION = 'Congratulations on your ownership of RUOYI No.'

background_type = ['Acidity', 'Cloth', 'Cyberpunk',
    'Gradual', 'Partysu', 'Smoke', 'Technology',
    'TriangularArray']
background_dict = {'Acidity':13, 'Cloth':7, 'Cyberpunk':17,
    'Gradual':8, 'Partysu':10, 'Smoke':35, 'Technology':8,
    'TriangularArray':10}

background_type_now = ''
combine_index_now = 0

def rand_background_address():
    global background_type_now

    rand_type_num = random.randint(1, len(background_type)) - 1
    rand_type = background_type[rand_type_num]
    rand_img_num = random.randint(1, background_dict[rand_type])
    rand_background_address = BACKGROUND_ADDRESS_PREFIX + rand_type + UNDERLINE + str(rand_img_num)
    background_type_now = rand_type

    if os.path.isfile(rand_background_address + '.jpg') :
        return rand_background_address + '.jpg'
    elif os.path.isfile(rand_background_address + '.png') :
        return rand_background_address + '.png'
    else :
        print("rand_background_address: " + rand_background_address + " is wrong!")

def get_ruoyi_address(index):
    ruoyi_address = RUOYI_ADDRESS_PREFIX + str(index) + ".png"
    return ruoyi_address

def img_combine(image_ruoyi_address, image_background_address, last_background_address):
    if image_background_address == last_background_address:
        img_combine(image_ruoyi_address, rand_background_address(), last_background_address)
    else:
        img_combine_inner(image_ruoyi_address, image_background_address)

def img_combine_inner(image_ruoyi_address, image_background_address):
    global combine_index_now
    # open img
    img_ruoyi = Image.open(image_ruoyi_address).convert('RGBA')
    img_background = Image.open(image_background_address).convert('RGBA')

    # resize background to matching RuoYi img
    background_width = img_background.width
    background_height = img_background.height
    if background_width > background_height:
        background_max = background_height
    else:
        background_max = background_width
    resize_min = random.randint(0,100)
    resize_max = random.randint(200, background_max)
    background_resize_box = (resize_min, resize_min, resize_max, resize_max)
    img_background_resize = img_background.resize((RESIZE_PIX, RESIZE_PIX), None, background_resize_box, reducing_gap=5.0)

    # combine RuoYi img and background img
    combine_index_now += 1
    img_combine_address = COMBINE_ADDRESS_PREFIX + str(combine_index_now) + UNDERLINE + background_type_now + ".png"
    Image.alpha_composite(img_background_resize, img_ruoyi).convert('RGB').save(img_combine_address)   
    add_nft_json() 

def add_nft_json():
    nft_name = JSON_NAME + str(combine_index_now)
    nft_discription = JSON_DESCRIPTION + str(combine_index_now)
    nft_ruoyi_attributes = find_ruoyi_attributes(combine_index_now)
    json_dict = {
        'name':nft_name, 
        'description':nft_discription, 
        'image':'ipfs://', 
        'attributes':[
            {'trait_type':'background', 'value':background_type_now},
            {'trait_type':'ruoyi', 'value':nft_ruoyi_attributes}
        ]
    }
    if combine_index_now < RUOYI_ALL_NUM:
        json_file.write(json.dumps(json_dict) + ',')
    else:
        json_file.write(json.dumps(json_dict))

def find_ruoyi_attributes(index):
    if 1 <= index <= 100:
        return 'Cute Camisole'
    elif 100 < index <= 200:
        return 'Fishnet'
    elif 200 < index <= 300:
        return 'JK'
    elif 300 < index <= 400:
        return 'Future Mecha'
    elif 400 < index <= 420:
        return 'Hanfu'
    elif 420 < index <= 440:
        return 'Elegant Sweater'
    elif 440 < index <= 460:
        return 'Flower Design & Necklace'
    elif 460 < index <= 480:
        return 'Maid'
    elif 480 < index <= 500:
        return 'Fishnet Clothes & Glasses'
    elif 500 < index <= 520:
        return 'Ninja'
    elif 520 < index <= 560:
        return 'Songfu'
    elif 560 < index <= 580:
        return 'Comfortable Home Cloth'
    elif 580 < index <= 600:
        return 'Elf Queen'
    elif 600 < index <= 620:
        return 'Hoodie'
    elif 620 < index <= 660:
        return 'Dress'
    elif 660 < index <= 670:
        return 'Swimsuit'
    elif 670 < index <= 680:
        return 'One-piece Swimsuit'
    elif 680 < index <= 700:
        return 'Leather'
    elif 700 < index <= 800:
        return 'Basketball Jersey'
    elif 800 < index <= 820:
        return 'Used JK'
    elif 820 < index <= 840:
        return 'Skeleton Dress'
    elif 840 < index <= 860:
        return 'Robust Battle Armor'
    elif 860 < index <= 880:
        return 'I Come From The Future'
    elif 880 < index <= 920:
        return 'Street Sweater & Mask'
    elif 920 < index <= 950:
        return 'Matured Me'
    elif 950 < index <= 980:
        return 'Denim'
    elif 980 < index <= 985:
        return 'Mage, Fireball!'
    elif 985 < index <= 990:
        return 'Tentacles, Kill Him!'
    elif 990 < index <= 995:
        return 'Knight, I Will Always Be Loyal!'
    elif 995 < index <= 1000:
        return 'Foreigner, Stay For Me!'
    elif 1000 < index <= 1010:
        return 'Spirituality Fluctuation!'
    elif 1010 < index <= 1013:
        return 'Mystery!'
    elif 1013 < index <= 1018:
        return 'Noble College!'
    elif index == 1019:
        return 'Daughter Of Flame!!'
    elif index == 1020:
        return 'Daughter Of Ice And Cool!!'
    elif index == 1021:
        return 'Darkness!!!'
    elif index == 1022:
        return 'Cyberpunk!!!'
    elif index == 1023:
        return 'Underground Fighter!!!'
    elif index == 1024:
        return 'Banana!!!'




if __name__ == '__main__':
    json_file = open(JSON_ADDRESS, 'a', encoding='utf-8')
    json_file.write('[')

    for index in range(1, RUOYI_IMG_ALL_NUM + 1):
        image_ruoyi_address = get_ruoyi_address(index)
        image_background_address = rand_background_address()
        img_combine(image_ruoyi_address, image_background_address, '')
        if index <= RUOYI_IMG_NORMAL_NUM:
            img_combine(image_ruoyi_address, rand_background_address(), image_background_address)
    
    json_file.write(']')
    json_file.close()