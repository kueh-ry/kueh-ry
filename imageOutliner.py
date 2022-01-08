from sketchify import sketch
import os
import pathlib

def main():
    rootDir = "{}\img".format(pathlib.Path().resolve())
    error = []
    for dirName, _, fileList in os.walk(rootDir):
        for fname in fileList:
            fullPath = "{}\{}".format(dirName, fname)
            path = "{}_proc".format(dirName.replace("+","_"))
            print(fullPath)
            print(path)
            isExist = os.path.exists(path)
            if not isExist and "_proc" not in fullPath:
                os.mkdir(path)
            try:
                sketch.normalsketch(fullPath, path, fname, scale=10)
            except:
                error.append((fullPath, path, fname))
                print("fail", fullPath, path, fname)
    print(len(error))
    print(error)


main()
