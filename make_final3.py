from PIL import Image
orig = Image.open('C:\\Users\\eedua\\.gemini\\antigravity\\brain\\e601729d-5752-4f6a-a67c-e3ddc80eb960\\enzima_gordura_antes_depois_3_1785149100776.png')
top_left = orig.crop((0, 60, 512, 452))
top_right = orig.crop((512, 60, 1024, 452))
scale = 0.65
new_w = int(512 * scale)
new_h = int((452 - 60) * scale)
top_left = top_left.resize((new_w, new_h), Image.Resampling.LANCZOS)
top_right = top_right.resize((new_w, new_h), Image.Resampling.LANCZOS)
final = Image.new('RGB', (1024, 1024), (232, 233, 227))
start_x = (1024 - (new_w * 2)) // 2
start_y = (1024 - new_h) // 2
final.paste(top_left, (start_x, start_y))
final.paste(top_right, (start_x + new_w, start_y))
final.save('C:\\Users\\eedua\\Downloads\\medical-spa-landing-30.aura.build\\assets\\new_antes_depois_6.png')
final.save('C:\\Users\\eedua\\Downloads\\medical-spa-landing-30.aura.build\\assets\\new_antes_depois_6.webp')
