from PIL import Image
img = Image.open('C:\\Users\\eedua\\Downloads\\medical-spa-landing-30.aura.build\\assets\\ad_botox.png')
h = img.height
w = img.width
top = 0
bot = h - 1
while img.getpixel((w//2, top))[:3] == (232, 233, 227): top += 1
while img.getpixel((w//2, bot))[:3] == (232, 233, 227): bot -= 1
print('Top bar height:', top, 'Bottom bar height:', h - bot - 1)
