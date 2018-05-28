import os

rootpaths = ["C:/Users/User/Desktop/nbvcxz2/SIMRunner/java_finalresults1/"]
mergedresultpath = "java_mergedresult.txt"

if __name__ == '__main__':
    with open(mergedresultpath,"w+") as fr:
        fr.write("this result file may contain duplicate lines\n")
        fr.write("\n")
        for rootpath in rootpaths:
            for path, dirs, files in os.walk(rootpath):
                for f in files:
                    fp = os.path.join(path, f)
                    with open(fp, "r+") as fi:
                        for line in fi:
                            fr.write(line)
                            fr.flush()