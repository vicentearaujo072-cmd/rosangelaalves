from PIL import Image
img = Image.open('C:\\Users\\eedua\\Downloads\\medical-spa-landing-30.aura.build\\assets\\ad_botox.png')
bg = (232, 233, 227)
left, top, right, bot = 1024, 1024, 0, 0
for y in range(1024):
    for x in range(1024):
        if img.getpixel((x,y))[:3] != bg:
            if x < left: left = x
            if x > right: right = x
            if y < top: top = y
            if y > bot: bot = y
print('Bbox:', left, top, right, bot)
