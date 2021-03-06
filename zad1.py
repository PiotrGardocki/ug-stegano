from stegano import lsb
from stegano import lsbset
from stegano.lsbset import generators
import time
import os
import os.path
from pathlib import Path

def encode_messure(func, img, img_out, message):
    original_size = os.stat(img).st_size
    start = time.time()
    try:
        func(img, message).save(img_out)
    except IndexError:
        print(f'message len {len(message)} too large for image size {original_size}')
        return
    end = time.time()
    print(f'encode time: {(end-start):.10f}s')
    new_size = os.stat(img_out).st_size
    diff = new_size - original_size
    print(f'size before = {original_size}, size after = {new_size} ' + ('(%+d)' % diff))

def decode_messure(func, img):
    if not os.path.exists(img):
        print('missing image')
        return

    print('images size =', os.stat(img).st_size)
    start = time.time()
    message = func(img)
    #print('Message =', message)
    end = time.time()
    print(f'decode time: {(end-start):.10f}s')

def encode_lsb(img, message):
    return lsb.hide(img, message)

def decode_lsb(img):
    return lsb.reveal(img)

def encode_lsb_eratosthenes(img, message):
    return lsbset.hide(img, message, generators.eratosthenes())

def decode_lsb_eratosthenes(img):
    return lsbset.reveal(img, generators.eratosthenes())

def encode_lsb_fibonacci(img, message):
    return lsbset.hide(img, message, generators.fibonacci())

def decode_lsb_fibonacci(img):
    return lsbset.reveal(img, generators.fibonacci())

def img_original_path(img):
    return 'img/' + img

def img_encoded_path(img, method_name, message_index):
    img = img.split('.')
    img.insert(1, '-' + str(message_index) + '.')
    img.insert(1, '-' + str(method_name))
    img = ''.join(img)
    return 'encoded_img/' + img

messages = [
    'pies',
    'ala ma kota',
    'jak ja kocham steganografie',
    'Somebody once told me, the world is gonna roll me I ain\'t the sharpest ' \
    'tool in the shed She was looking kind of dumb with her finger and her ' \
    'thumb In the shape, of an "L" on her forehead',
    'a' * 5000,
]
images = [
    'house.png',
    'cup.png',
    'space.png',
    'tree.png',
]
methods = [
    ('LSB', encode_lsb, decode_lsb),
    ('LSB-eratosthenes', encode_lsb_eratosthenes, decode_lsb_eratosthenes),
    ('LSB-fibonacci', encode_lsb_fibonacci, decode_lsb_fibonacci),
]

Path("encoded_img").mkdir(exist_ok=True)

print('=== Encoding ===\n')
for method in methods:
    k = 1
    print('Testing method:', method[0])
    for image in images:
        for i, message in enumerate(messages):
            print(f'---\ntest #{str(k)}, message len = {len(message)}')
            encode_messure(method[1], img_original_path(image),
                           img_encoded_path(image, method[0], i), message)
            k += 1
    print()

print('=== Decoding ===')
for method in methods:
    k = 1
    print('Testing method:', method[0])
    for image in images:
        for i, message in enumerate(messages):
            print(f'---\ntest #{str(k)}, message len = {len(message)}')
            decode_messure(method[2], img_encoded_path(image, method[0], i))
            k += 1
    print()
