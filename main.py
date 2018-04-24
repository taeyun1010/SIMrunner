from subprocess import call
# Function which returns subset or r length from n
from itertools import combinations

coins = ["bitcoin", "BTCGPU", "rippled"]
r = 2

# put extension of the file that will be compared
extension = "cpp"

def rSubset(arr, r):
 
    # return list of all subsets of length r
    # to deal with duplicate subsets use 
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))

# gets percentage given line, returns int type
def getPercentage(line):
    index = thisline.find("consists for")
    index = index + 13
    split = thisline[index:]
    endindex = split.find("%") - 1
    return int(split[:endindex])

# gets first file's extension, or "" if no file extension found 
def getFirstFileExtension(line):
    extension = ""
    index = line.find("consists for")
    endindex = index - 1
    while(1):
        if (index == -1):
            break
        thischar = line[index:(index+1)]
        if (thischar == "."):
            break
        index = index - 1
    
    
    # if dot is found
    if (index != -1):
        extension = line[(index+1):endindex]
    return extension

# gets second file's extension, or "" if no file extension found 
def getSecondFileExtension(line):
    extension = ""
    index = line.find(" material")
    endindex = index
    while(1):
        if (index == -1):
            break
        thischar = line[index:(index+1)]
        if (thischar == "."):
            break
        index = index - 1
    
    
    # if dot is found
    if (index != -1):
        extension = line[(index+1):endindex]
    return extension

# returns 1 if both file have wanted extension, 0 if first file does not, -1 if second file does not, 0 if both do not
def meetsRequirement(line):
#     print("line = " + line)
#     print("First file's extension = " + getFirstFileExtension(line))
#     print("Second file's extension = " + getSecondFileExtension(line))
    if ((getFirstFileExtension(line) == extension) and (getSecondFileExtension(line) == extension)):
        return 1
    if (getFirstFileExtension(line) != extension):
        return 0
    return -1

# gets a path to the first file
def getFirstFile(line):
    index = line.find("consists for")
    return line[:(index - 1)]

# gets a path to the second file
def getSecondFile(line):
    beginindex = line.find("% of") + 5
    endindex = line.find(" material")
    return line[beginindex:endindex]

if __name__ == '__main__':
    directorypath = "C:\Users\User\Desktop\sim_exe_3_0_2\coins/"
    combi = rSubset(coins, r)
    for thiscombi in combi:
        totalsum = 0
        count = 0
        print(thiscombi)
        coin1path = directorypath+ thiscombi[0] 
        coin2path = directorypath + thiscombi[1] 
        call(["C:\Users\User\Desktop\sim_exe_3_0_2\sim_c++.exe", "-p", "-a", "-R","-o","result.txt", coin1path, coin2path])
        with open("result.txt", "r+") as fi:
            while(1):
                line = fi.readline()
                if(line[:12] == "Total input:"):
                    break
            with open("processedresult.txt", "w+") as fo:
                coin1 = "coins/"+thiscombi[0]
                coin2 = "coins/"+thiscombi[1]
                for thisline in fi:
                    # write only if the line contains both coins being compared
                    if ((coin1 in thisline) and (coin2 in thisline)):
                        count = count + 1
                        p = getPercentage(thisline)
                        totalsum = totalsum + p
                        fo.write(thisline)
            f = open("processedresult.txt", "r")
            lines = f.readlines()
            f.close
            firstline = lines[0]
            
            requirementResult = meetsRequirement(firstline)
            
            # if has wanted extension
            if (requirementResult == 1):
                print("meets requirement")
            # else, delete all the lines containing the file with not wanted extension
            else:
                with open("processedresult.txt", "w+") as fo:
                    if (requirementResult == 0):
                        filetodelete = getFirstFile(firstline)
                    else:
                        filetodelete = getSecondFile(firstline)
                    for line in lines:
                        if filetodelete not in line:
                            fo.write(line)
            
            print("Similarity percentage between " + thiscombi[0] + " and " + thiscombi[1] + " = " + str((totalsum / count)))