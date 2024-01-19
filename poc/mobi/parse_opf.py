import xml.etree.ElementTree as ET

# File path for the OPF file
opf_file_path = 'test.opf'

# Read the content of the OPF file
with open(opf_file_path, 'r', encoding='utf-8') as file:
    opf_data = file.read()

# Parse the XML
root = ET.fromstring(opf_data)

# Define the namespace
ns = {'dc': 'http://purl.org/dc/elements/1.1/'}

# Find the title and creator
title = root.find('.//dc:title', ns).text
creator = root.find('.//dc:creator', ns).text
published_date = root.find('.//dc:date', ns).text
description = root.find('.//dc:description', ns).text

print(f"Title: {title}")
print(f"Creator: {creator}")
print(f"Published Date: {published_date}")
print(f"Description: {description}")
