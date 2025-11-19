import json
from pathlib import Path

def add_file_name(in_path, out_path):
    in_path = Path(in_path)
    out_path = Path(out_path)
    print(f"Processing {in_path} -> {out_path}")

    with in_path.open("r") as f:
        data = json.load(f)

    fixed = 0
    for img in data["images"]:
        if "file_name" not in img:
            coco_url = img.get("coco_url", "")
            if not coco_url:
                continue
            # Example: "http://images.cocodataset.org/train2017/000000391895.jpg"
            # We want "000000391895.jpg"
            img["file_name"] = coco_url.split("/")[-1]
            fixed += 1

    print(f"Added file_name for {fixed} images (out of {len(data['images'])}).")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        json.dump(data, f)
    print("Done.")

root = "/home/yj/ML/coco" # Modify to your own path

add_file_name(
    f"{root}/lvis_v1_train.json",
    f"{root}/lvis_v1_train_with_filenames.json"
)
add_file_name(
    f"{root}/lvis_v1_val.json",
    f"{root}/lvis_v1_val_with_filenames.json"
)