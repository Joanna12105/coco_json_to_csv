# https://stackoverflow.com/questions/15679467/parse-all-the-xml-files-in-a-directory-one-by-one-using-elementtree
import xml.etree.ElementTree as ET
import csv
import os

path_folder = "/content/images/"
csv_filename = "org_imgs_bb.csv"

with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    writer.writerow(['Folder', 'Filename', 'Path', 'Source', 'Width', 'Height', 'Depth', 'Segmented', 
                     'Object Name', 'Object Pose', 'Object Truncated', 'Object Difficult', 'Bounding Box'])
  
    for object_detection_file in os.listdir(path_folder):
      if not object_detection_file.endswith(".xml"):
        continue

      path_file = os.path.join(path_folder, object_detection_file)
      tree = ET.parse(path_file)
      root = tree.getroot()    
      
      folder = root.find('folder').text
      filename = root.find('filename').text
      path = root.find('path').text
      source_root = root.find('source')
      source = source_root.find('database').text
      size = root.find('size')
      width = size.find('width').text
      height = size.find('height').text
      depth = size.find('depth').text
      segmented = root.find('segmented').text
      
      for obj in root.findall('object'):
          name = obj.find('name').text
          pose = obj.find('pose').text
          truncated = obj.find('truncated').text
          difficult = obj.find('difficult').text
          bndbox = obj.find('bndbox')
          xmin = bndbox.find('xmin').text
          ymin = bndbox.find('ymin').text
          xmax = bndbox.find('xmax').text
          ymax = bndbox.find('ymax').text
          
          bbox = f'[{xmin}, {ymin}, {xmax}, {ymax}]'
          
          writer.writerow([folder, filename, path, source, width, height, depth, segmented, 
                           name, pose, truncated, difficult, bbox])
