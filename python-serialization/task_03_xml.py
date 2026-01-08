#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")  # Create the root element
    for key, value in dictionary.items():
        # Create child elements for each dictionary item
        child = ET.SubElement(root, key)
        child.text = str(value)  # Store the value as text (convert to string)
    
    tree = ET.ElementTree(root)
    tree.write(filename)  # Write the XML tree to the file

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        # Convert the XML elements back into a dictionary
        data = {}
        for child in root:
            data[child.tag] = child.text
        return data
    except ET.ParseError:
        print(f"Error parsing XML from {filename}")
        return None
