#!/usr/bin/env python

from lxml import etree
import os
import sys
import hashlib
import StringIO

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
        return sha256.hexdigest()

if len(sys.argv) != 2:
    print("Product name is required")
    sys.exit(1)

product = sys.argv[1]
tree = etree.parse("/tmp/test.xml")
root = tree.getroot()
print(root)
for package in root:
    print(package[10].attrib['href'])
    if(os.path.isfile("/repo/" + product + "/" + package[10].attrib['href'])):
	found_sha256 = sha256_checksum("/repo/" + product + "/" + package[10].attrib['href'])
	if (found_sha256 == package[3].text):
	    print("OK");
        else:
            print("Delete : %s" % ("/repo/" + product + "/" + package[10].attrib['href']))
            os.remove("/repo/" + product + "/" + package[10].attrib['href'])
