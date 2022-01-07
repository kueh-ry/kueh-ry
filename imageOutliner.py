from sketchify import sketch
import os
import pathlib

def main():
    rootDir = "{}\img".format(pathlib.Path().resolve())
    for dirName, _, fileList in os.walk(rootDir):
        for fname in fileList:
            fullPath = "{}\{}".format(dirName, fname)
            path = "{}_proc".format(dirName)
            isExist = os.path.exists(path)
            if not isExist:
                os.mkdir(path)
            sketch.normalsketch(fullPath, path, "{}.jpg".format(fname))

main()
