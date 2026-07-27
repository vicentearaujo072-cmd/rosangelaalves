from PIL import Image
img = Image.open('C:\\Users\\eedua\\.gemini\\antigravity\\brain\\e601729d-5752-4f6a-a67c-e3ddc80eb960\\enzima_gordura_antes_depois_3_1785149100776.png')
img_cropped = img.crop((0, 150, 1024, 1024-150))
new_img = Image.new('RGB', (1024, 1024), (232, 233, 227))
new_img.paste(img_cropped, (0, 150))
new_img.save('C:\\Users\\eedua\\Downloads\\medical-spa-landing-30.aura.build\\assets\\new_antes_depois_6.png')
new_img.save('C:\\Users\\eedua\\Downloads\\medical-spa-landing-30.aura.build\\assets\\new_antes_depois_6.webp')
