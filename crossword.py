from PIL import Image, ImageDraw, ImageFont, ImageColor
import random



def sirala(e):
  return len(e)
bg1 = Image.new('RGBA', (10, 10), color='black')
font = ImageFont.truetype("arial.ttf", size=42)

liste = ["APPLE","HOUSE","DOOR","ANIMAL","MONEY","SHUFFLE","BIOLOGY","ONE"]
liste.sort(reverse=True, key=sirala)

kackelime = len(liste)
enuzun = len(liste[0])

allmerge = []

for p in liste:
	resimler = []
	count = 1
	for i in p:
		font = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", 160)
		im = Image.new("RGB", (200, 200), "white")
		d = ImageDraw.Draw(im)
		d.line(((10, 10), (10, 194)), "black", width=8)
		d.line(((10, 190), (190, 190)), "black", width=8)
		d.line(((7, 10), (190, 10)), "black", width=8)
		d.line(((190, 7), (190, 194)), "black", width=8)
		d.text((100, 100), "{}".format(i), fill="black", anchor="mm", font=font)

		im.save('{}-{}-{}.png'.format(p,i,count))
		resimler.append("{}-{}-{}.png".format(p,i,count))
		count = count + 1

	mergewidth = len(resimler)*200
	print(resimler)
	bg = Image.new('RGB',(mergewidth, 200), (250,250,250))

	countsize = 0
	for i in resimler:
		print(i)
		head_crop = Image.open("{}".format(i))
		bg.paste(head_crop,(countsize,0))
		countsize= countsize +200

	bg.save("{}.jpg".format(p),"JPEG")
	allmerge.append("{}.jpg".format(p))

countsize2 = 0
bg = Image.new('RGB',(enuzun*200, kackelime*200), (0,0,0))
random.shuffle(allmerge)
for m in allmerge:
	head_crop = Image.open("{}".format(m))
	bg.paste(head_crop,(0,countsize2))
	countsize2 = countsize2 + 200

bg.save("{}.jpg".format("final"),"JPEG")
