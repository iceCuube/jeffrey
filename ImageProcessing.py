from ast import Bytes
from sre_parse import HEXDIGITS
from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageFilter
from io import BytesIO

base_img = Image.open("assets/livereactionbase.jpg") # keep base image in memory
font = ImageFont.truetype("assets/Futura Bold.otf", 135)

def livereaction(pfp: BytesIO, name: str) -> BytesIO:
	img = base_img.copy()
	pfp_img = Image.open(pfp) 

	txt = "LIVE " + name.upper() + " REACTION"
	size = font.getsize(txt)

	# --- TEXT ---
	redbox = Image.new("RGB", (size[0], size[1]+5), color=ImageColor.getrgb("#af1e23"))
	draw = ImageDraw.Draw(redbox)
	draw.text((0,0), txt, font=font, fill=(0,0,0,100))
	redbox = redbox.filter(ImageFilter.GaussianBlur(radius=5))
	draw = ImageDraw.Draw(redbox) # get handle again
	draw.text((0,0), txt, font=font, fill=ImageColor.getrgb('#ffffffff'))
	redbox = redbox.resize((1009, 122))
	#redbox.show()

	# --- PFP ---
	pfp_img = pfp_img.resize((1042, 595))

	# start pasting the images
	img.paste(redbox, (33,30))
	img.paste(pfp_img, (19, 184))

	img_bytes = BytesIO()
	img.save(img_bytes,
		format ="JPEG", 
		progression = True,
		quality = 30
	)
	img_bytes.seek(0)
	return img_bytes