import os

OLD_NAMES = ['clean', 'clutter', 'glass', 'paper', 'plastic']
DROP = {'clean', 'clutter'}
NEW_NAMES = [n for n in OLD_NAMES if n not in DROP]

# old_id -> new_id (or None if dropped)
remap = {}
new_idx = 0
for old_idx, name in enumerate(OLD_NAMES):
    if name in DROP:
        remap[old_idx] = None
    else:
        remap[old_idx] = new_idx
        new_idx += 1

BASE = r'my_raw_data\SMART ZONE-WISE MESS DETECTION.v1i.yolov8'


def process_split(labels_dir, images_dir):
    if not os.path.isdir(labels_dir):
        print(f"Skipping (not found): {labels_dir}")
        return

    removed_files = 0
    kept_files = 0

    for fname in os.listdir(labels_dir):
        if not fname.endswith('.txt'):
            continue
        path = os.path.join(labels_dir, fname)
        kept_lines = []
        with open(path) as f:
            for line in f:
                parts = line.strip().split()
                if not parts:
                    continue
                old_cls = int(parts[0])
                new_cls = remap.get(old_cls)
                if new_cls is not None:
                    parts[0] = str(new_cls)
                    kept_lines.append(' '.join(parts))

        if kept_lines:
            with open(path, 'w') as f:
                f.write('\n'.join(kept_lines) + '\n')
            kept_files += 1
        else:
            os.remove(path)
            base_name = os.path.splitext(fname)[0]
            for ext in ('.jpg', '.jpeg', '.png'):
                img_path = os.path.join(images_dir, base_name + ext)
                if os.path.exists(img_path):
                    os.remove(img_path)
                    break
            removed_files += 1

    print(f"{labels_dir}: kept {kept_files}, removed {removed_files} (no remaining boxes)")


for split in ['train', 'test']:
    process_split(
        os.path.join(BASE, split, 'labels'),
        os.path.join(BASE, split, 'images'),
    )

print("New class order:", NEW_NAMES)