import py7zr
import os
import json

def readPackageHeader(packageFilename, packageName):
    with(py7zr.SevenZipFile(packageFilename, mode='r') as z):
        text = z.read(targets=[packageName + "/package.json"])[packageName + "/package.json"].read()
        jsonL = json.loads(text)
        output = dict()
        output["name"] = jsonL["name"]
        output["version"] = jsonL["version"]
        output["description"] = jsonL["description"]
        output["dependencies"] = jsonL["dependencies"]
        output["platform"] = packageName.replace(jsonL["name"] + "-", "")
        return output;

output = []
for filename in os.listdir():
    if(filename[-3:] == ".7z"):
        output.append(readPackageHeader(filename, filename[:-3]))

output_text = json.dumps(output)

with(open("listings.json", "w") as listingsFile):
    listingsFile.write(output_text)

print(output_text)
