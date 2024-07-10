# https://blog.finxter.com/5-best-ways-to-convert-python-csv-to-xml-using-elementtree/
import csv
import xml.etree.ElementTree as ET

csv_path = "/content/org_imgs_bb.csv"

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    get_filenames = None
    for row in csv_reader: 
      get_filenames = [row['Filename']].append(row)
      for xml_file, rows in get_filenames.items():
       
      root = ET.Element('annotation')
      
      ET.SubElement(root, 'folder').text = first_row['Folder']
      ET.SubElement(root, 'filename').text = first_row['Filename']
      ET.SubElement(root, 'path').text = first_row['Path']
      
      source = ET.SubElement(root, 'source')
      ET.SubElement(source, 'database').text = 'Unknown'
      
      size = ET.SubElement(root, 'size')
      ET.SubElement(size, 'width').text = first_row['Width']
      ET.SubElement(size, 'height').text = first_row['Height']
      ET.SubElement(size, 'depth').text = first_row['Depth']
      
      ET.SubElement(root, 'segmented').text = first_row['Segmented']
      
      for row in reader:
          obj = ET.SubElement(root, 'object')
          ET.SubElement(obj, 'name').text = row['Object Name']
          ET.SubElement(obj, 'pose').text = row['Pose']
          ET.SubElement(obj, 'truncated').text = row['Truncated']
          ET.SubElement(obj, 'difficult').text = row['Difficult']
          
          bndbox = ET.SubElement(obj, 'bndbox')
          bbox = eval(row['Bounding Box'])  # Convert the string back to list
          ET.SubElement(bndbox, 'xmin').text = str(bbox[0])
          ET.SubElement(bndbox, 'ymin').text = str(bbox[1])
          ET.SubElement(bndbox, 'xmax').text = str(bbox[2])
          ET.SubElement(bndbox, 'ymax').text = str(bbox[3])
      
      tree = ET.ElementTree(root)
      tree.write('output.xml')
