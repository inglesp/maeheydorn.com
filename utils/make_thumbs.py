import os, sys
from PIL import Image


for fn in sys.argv[1:]:
    image = Image.open(fn)
    w, h = image.size
    if w > h:
        new_w = 200
        new_h = int(h * new_w / w)
    else:
        new_h = 200
        new_w = int(w * new_h / h)

    basename, ext = os.path.splitext(fn)
    new_fn = basename + '_thumb' + ext

    thumb = image.resize((new_w, new_h))
    thumb.save(new_fn)
