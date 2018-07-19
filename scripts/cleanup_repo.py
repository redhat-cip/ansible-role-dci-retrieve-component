#!/usr/bin/env python

from lxml import etree
import os
import hashlib
import StringIO

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
        return sha256.hexdigest()

tree = etree.parse("/tmp/test.xml")
root = tree.getroot()
print(root)
for package in root:
    print(package[10].attrib['href'])
    if(os.path.isfile("/repo/rhel/" + package[10].attrib['href'])):
	found_sha256 = sha256_checksum("/repo/rhel/" + package[10].attrib['href'])
	if (found_sha256 == package[3].text):
	    print("OK");
        else:
            print("Delete : %s" % ("/repo/rhel/" + package[10].attrib['href']))
            os.remove("/repo/rhel/" + package[10].attrib['href'])
