import os
from PIL import Image

path = 'static/img/'
names = os.listdir(path)

height = 200

for n in names:
    base, ext = os.path.splitext(n)
    tn = base + '_thumb' + ext
    if 'thumb' in n or tn in names:
        continue

    im = Image.open(path + n)

    width = height * im.width / im.height
    size = (width, height)

    im.thumbnail(size, Image.ANTIALIAS)
    im.save(path + tn)
