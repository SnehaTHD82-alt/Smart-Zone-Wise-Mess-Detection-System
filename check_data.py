import os
from collections import Counter

BASE = r'my_raw_data\SMART ZONE-WISE MESS DETECTION.v1i.yolov8'
names = ['glass', 'paper', 'plastic']

for split in ['train', 'valid', 'test']:
    lbl_dir = os.path.join(BASE, split, 'labels')
    counts = Counter()
    n_images = 0
    if os.path.isdir(lbl_dir):
        for fname in os.listdir(lbl_dir):
            n_images += 1
            with open(os.path.join(lbl_dir, fname)) as f:
                for line in f:
                    if line.strip():
                        counts[int(line.split()[0])] += 1
    print(f"\n{split} ({n_images} label files):")
    for i, n in enumerate(names):
        print(f"  {n}: {counts.get(i, 0)}")