from subprocess import call
# Function which returns subset or r length from n
from itertools import combinations
import os
import multiprocessing
import time
import signal
from utils import delay
import thread
from twisted.internet.test.reactormixins import process
#from eventlet.timeout import Timeout

#coins = ["bitcoin", "BTCGPU", "rippled", "BitcoinDiamond", "BitcoinPrivate", "bytecoin", "litecoin", "nano"]
r = 2

#change the home directory of coins
directorypath = "C:/Users/User/Desktop/test_coins/c/"

# put extension of the file that will be compared
#extension = "cpp"
extension = ["c", "cpp", "h", "cc"]

def rSubset(arr, r):
 
    # return list of all subsets of length r
    # to deal with duplicate subsets use 
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))

# gets percentage given line, returns int type
def getPercentage(line):
    #index = thisline.find("for ")
    #index = index
    #split = thisline[index:]
#     endindex = split.find("%")-1
#     split = split[:endindex]
    p = [int(s) for s in line.split() if s.isdigit()]
    #print(split[:endindex])
    #return int(split[:endindex])
    return p[0]

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

# old version that uses only 1 file extension
# # returns 1 if both file have wanted extension, 0 if first file does not, -1 if second file does not, 0 if both do not
# def meetsRequirement(line):
# #     print("line = " + line)
# #     print("First file's extension = " + getFirstFileExtension(line))
# #     print("Second file's extension = " + getSecondFileExtension(line))
#     if ((getFirstFileExtension(line) == extension) and (getSecondFileExtension(line) == extension)):
#         return 1
#     if (getFirstFileExtension(line) != extension):
#         return 0
#     return -1


# returns 1 if both file have wanted extension, 0 if first file does not, -1 if second file does not, 0 if both do not
def meetsRequirement(line):
#     print("line = " + line)
#     print("First file's extension = " + getFirstFileExtension(line))
#     print("Second file's extension = " + getSecondFileExtension(line))
    firstfile = 0
    secondfile = 0
    for ext in extension:
        if (getFirstFileExtension(line) == ext):
            firstfile = 1
            break
    for ext in extension:
        if (getSecondFileExtension(line) == ext):
            secondfile = 1
            break    
    if ((firstfile == 1) and (secondfile == 1)):
        return 1
    if (firstfile == 0):
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

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

@delay(10.0)
def callSIM(coin1path, coin2path):
    call(["C:\Users\User\Desktop\sim_exe_3_0_2\sim_c++.exe", "-p", "-a", "-R","-o","result.txt", coin1path, coin2path])

def handler(signum, frame):
    print "Forever is over!"
    raise Exception("end of time")

def compare(coin1, coin2):
#     directorypath = "C:\Users\User\Desktop\sim_exe_3_0_2\coins/"
    
 
    print(coin1 + coin2)
    finalresultpath = "finalresults/" + coin1 + "_" + coin2 + "_finalresult.txt"
    resultpath = coin1 + "_" + coin2 + "_result.txt"
    processedresultpath = coin1 + "_" + coin2 + "_processedresult.txt"
    with open(finalresultpath,"w+") as fr:
       
        totalsum = 0
        count = 0
        coin1path = directorypath+ coin1
        coin2path = directorypath + coin2 
        #print("coin1path = " + coin1path)
        #print("coin2path = " + coin2path)


        call(["C:\Users\User\Desktop\sim_exe_3_0_2\sim_c++.exe", "-p", "-a", "-R","-o",resultpath, coin1path, coin2path])
#             callSIM(coin1path, coin2path)
         # Start foo as a process
       



#             p = multiprocessing.Process(target=callSIM, name="callSIM", args=(coin1path, coin2path))
#             p.start()
#         
#             # Wait 10 seconds for foo
#             time.sleep(100)
#             continue
#             # Terminate foo
#             p.terminate()
#          
#             # Cleanup
#             p.join()

       
       
       
        with open(resultpath, "r+") as fi:
            while(1):
                line = fi.readline()
                if(line[:12] == "Total input:"):
                    break
            with open(processedresultpath, "w+") as fo:
                
                for thisline in fi:
                    # write only if the line contains both coins being compared
                    if ((coin1 in thisline) and (coin2 in thisline)):
                        #count = count + 1
                        #p = getPercentage(thisline)
                        #totalsum = totalsum + p
                        fo.write(thisline)
                        
            while(1):
                f = open(processedresultpath, "r")
                lines = f.readlines()
                f.close
                if (len(lines) == 0):
                    break
                firstline = lines[0]
                
                requirementResult = meetsRequirement(firstline)
                filetosearch = getFirstFile(firstline)
                
                # if has wanted extension
                if (requirementResult == 1):
                    count = count + 1
                    maxpercentage = 0
                    for line in lines:
                        if (filetosearch == getFirstFile(line)):
                            if (meetsRequirement(line) == 1):
                                thispercentage = getPercentage(line)
                                if (thispercentage > maxpercentage):
                                    maxpercentage = thispercentage
                    #print(filetosearch + " showed max of " + str(maxpercentage) + " similarity \n")
                    totalsum = totalsum + maxpercentage
                    # done with this file, delete all lines containing this file as first file
                    with open(processedresultpath, "w+") as fo:
                        for line in lines:
                            if (getFirstFile(line) != filetosearch):
                                fo.write(line)
                    
                # else, delete all the lines containing the file with not wanted extension
                else:
                    with open(processedresultpath, "w+") as fo:
                        if (requirementResult == 0):
                            filetodelete = getFirstFile(firstline)
                        else:
                            filetodelete = getSecondFile(firstline)
                        for line in lines:
                            if filetodelete not in line:
                                fo.write(line)
            if (count != 0):
                fr.write("Similarity percentage between " + coin1 + " and " + coin2 + " = " + str((totalsum / count)) + "\n")
                fr.flush()
            else:
                fr.write("Similarity percentage between " + coin1 + " and " + coin2 + " = count was zero!!!!!!" + "\n")
                fr.flush()
        