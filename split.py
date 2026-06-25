import os
import random
import shutil

BASE = r'my_raw_data\SMART ZONE-WISE MESS DETECTION.v1i.yolov8'
VAL_RATIO = 0.15  # 15% of train goes to validation

train_img_dir = os.path.join(BASE, 'train', 'images')
train_lbl_dir = os.path.join(BASE, 'train', 'labels')
val_img_dir = os.path.join(BASE, 'valid', 'images')
val_lbl_dir = os.path.join(BASE, 'valid', 'labels')

os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_lbl_dir, exist_ok=True)

images = [f for f in os.listdir(train_img_dir)
          if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
random.seed(42)
random.shuffle(images)

n_val = int(len(images) * VAL_RATIO)
val_images = images[:n_val]

for img_name in val_images:
    base_name = os.path.splitext(img_name)[0]
    lbl_name = base_name + '.txt'

    src_img = os.path.join(train_img_dir, img_name)
    src_lbl = os.path.join(train_lbl_dir, lbl_name)

    shutil.move(src_img, os.path.join(val_img_dir, img_name))
    if os.path.exists(src_lbl):
        shutil.move(src_lbl, os.path.join(val_lbl_dir, lbl_name))

print(f"Moved {len(val_images)} images (of {len(images)} total) to valid/")