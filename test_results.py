import os

path = "C:/Users/User/Desktop/nbvcxz2/SIMRunner/go_finalresults1/"

if __name__ == '__main__':
    for path, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(path, f)
#             print(fp)
            with open(fp, "r+") as fi:
                for line in fi:
                    if ("count was zero" in line):
                        break
                    else:
                        print(line)
            