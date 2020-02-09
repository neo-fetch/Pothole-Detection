import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET
print("is good")

def write_xml(folder, img, objects, tl, br, saveddir):
    print("is good")
    if not os.path.isdir(saveddir):
        os.mkdir(saveddir)

    image = cv2.imread(img.path)
    height, width, depth = image.shape
    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = img.name
    ET.SubElement(annotation, 'segmented').text = '0'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)

    for obj,topl,botr in zip(objects,tl,br):
        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = obj
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox,'xmin').text = str(topl[0])
        ET.SubElement(bbox,'ymin').text = str(topl[1])
        ET.SubElement(bbox,'xmax').text = str(botr[0])
        ET.SubElement(bbox,'ymax').text = str(botr[1])

        xml_str = ET.tostring(annotation)
        root = etree.fromstring(xml_str)
        xml_str = etree.tostring(root, pretty_print = True)
        return xml_str

if __name__ == "__main__":
    print(" is good")
    folder = '/home/mayank/potholes/pothole_image_data/MyDataset/train/mayank/'
    img = [im for im in os.scandir('/home/mayank/potholes/pothole_image_data/MyDataset/train/mayank/')][0]
    objects = ['POTHOLE']
    tl = [(10,10)]
    br = [(100, 100)]
    saveddir = '/home/mayank/potholes/pothole_image_data/MyDataset/train/mkannotations/'
               
    xml_str = write_xml(folder, img, objects, tl, br, saveddir)
    
    print(xml_str)