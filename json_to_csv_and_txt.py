import argparse
import json

parser = argparse.ArgumentParser(description='Convert COCO annotations to CSV format.')
parser.add_argument('filename', type=str, help='The filename to process')
parser.add_argument('--categories', nargs='+', type=int, help='List of category IDs to filter')
args = parser.parse_args()
input_filename = args.filename
categories = args.categories if args.categories else None

with open(input_filename) as f:
    data = json.load(f)

images = {}
for img in data["images"]:
    id = img["id"]
    width = img["width"]
    height = img["height"]
    filename = img["file_name"]
    images[id] = {"id": id, "width": width, "height": height, "filename": filename, "annotations": []}

for ann in data["annotations"]:
    id = ann["image_id"]
    x_min = ann["bbox"][0]
    y_min = ann["bbox"][1]
    x_max = x_min + ann["bbox"][2]
    y_max = y_min + ann["bbox"][3]
    category = str(ann["category_id"])
    if categories and category not in categories:
        continue
    images[id]["annotations"].append(
        {"x_min": x_min, "y_min": y_min, "x_max": x_max, "y_max": y_max, "class": category})

with open(input_filename.replace("json", "csv"), "w") as f:
    f.write("filename,width,height,class,xmin,ymin,xmax,ymax\n")
    for img in images.values():
        for ann in img["annotations"]:
            f.write(
                f"{img['filename']},{img['width']},{img['height']},{ann['class']},{ann['x_min']},{ann['y_min']},{ann['x_max']},{ann['y_max']}\n")

with open(input_filename.replace("json", "txt"), "w") as f:
    for img in images.values():
        if len(img["annotations"]) > 0:
            f.write(f"{img['filename']}\n")
            
