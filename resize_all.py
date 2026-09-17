import os
from PIL import Image

# 設定目標尺寸 (適合卡片的 2x 銳利尺寸)
TARGET_SIZE = (96, 96)
# 支援的副檔名
EXTS = ('.png', '.jpg', '.jpeg', '.webp')

# 圖片來源與輸出資料夾
input_dir = "images"
output_dir = "resized"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(EXTS):
        img_path = os.path.join(input_dir, filename)
        with Image.open(img_path) as img:
            img = img.convert('RGBA')
            img.thumbnail(TARGET_SIZE, Image.Resampling.LANCZOS)
            
            # 建立透明畫布並將縮小後的圖居中貼上
            new_img = Image.new('RGBA', TARGET_SIZE, (0, 0, 0, 0))
            paste_x = (TARGET_SIZE[0] - img.width) // 2
            paste_y = (TARGET_SIZE[1] - img.height) // 2
            new_img.paste(img, (paste_x, paste_y), mask=img)
            
            output_path = os.path.join(output_dir, filename)
            new_img.save(output_path, 'PNG')
            print(f"✔ 已處理: {filename}")

print("\n全部完成！已儲存在 resized 資料夾。")