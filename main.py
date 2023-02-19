from pilmoji import Pilmoji
from PIL import Image, ImageFont
import numpy as np


emoji = "👓"
# shoggoth image used for testing was https://twitter.com/repligate/status/1626612235647819776
shogg = Image.open(r"shoggoth.png").convert("RGBA")
mask = Image.open(r"mask.png").convert("RGBA")

# feel free to change the background color to suit your emoji
# set to the RGBA values for the base smile emojis.
with Image.new('RGBA', (56, 61), (0xff, 0xcc, 0x4d, 0xff)) as image:
    font = ImageFont.truetype('arial.ttf', 24)
    # Change the (x, y) to offset the emoji, or scale_factor to scale it up or down.
    with Pilmoji(image) as pilmoji:
        pilmoji.text((-2, 0), emoji.strip(), (0, 0, 0, 0), font, emoji_scale_factor=2.65, embedded_color=True)
    im2arr = np.array(image)
    mask2arr = np.array(mask)
    im2arr[np.mean(mask2arr, axis=2) != 255] = mask2arr[np.mean(mask2arr, axis=2) != 255]
    shogg2arr = np.array(shogg)
    shogg2arr[236:236+61, 24:24+56] = im2arr
    image = Image.fromarray(shogg2arr)
    image.save("peachggoth.png")
    image.show()