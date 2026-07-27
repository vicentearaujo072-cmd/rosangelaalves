from PIL import Image
orig = Image.open('C:\\Users\\eedua\\.gemini\\antigravity\\brain\\e601729d-5752-4f6a-a67c-e3ddc80eb960\\enzima_gordura_antes_depois_3_1785149100776.png')
top_left = orig.crop((0, 0, 512, 512))
top_right = orig.crop((512, 0, 1024, 512))
final = Image.new('RGB', (1024, 1024), (232, 233, 227))
final.paste(top_left, (0, 256))
final.paste(top_right, (512, 256))
final.save('C:\\Users\\eedua\\Downloads\\medical-spa-landing-30.aura.build\\assets\\new_antes_depois_6.png')
final.save('C:\\Users\\eedua\\Downloads\\medical-spa-landing-30.aura.build\\assets\\new_antes_depois_6.webp')
