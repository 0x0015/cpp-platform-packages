import py7zr
import os
import json

def readPackageHeader(packageFilename, packageName):
    with(py7zr.SevenZipFile(packageFilename, mode='r') as z):
        text = z.read(targets=[packageName + "/package.json"])[packageName + "/package.json"].read()
        return json.loads(text)

output = []
for filename in os.listdir():
    if(filename[-3:] == ".7z"):
        output.append(readPackageHeader(filename, filename[:-3]))

output_text = json.dumps(output)

with(open("listings.json", "w") as listingsFile):
    listingsFile.write(output_text)

print(output_text)
