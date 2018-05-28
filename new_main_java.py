from subprocess import call
# Function which returns subset or r length from n
from itertools import combinations
import os
import multiprocessing
import time
import signal
from utils import delay
import threading
import Queue

# TODO
from main_old_java import compare
import subprocess
import sys
#from eventlet.timeout import Timeout

#coins = ["bitcoin", "BTCGPU", "rippled", "BitcoinDiamond", "BitcoinPrivate", "bytecoin", "litecoin", "nano"]
r = 2

#change the home directory of coins
directorypath = "C:/Users/User/Desktop/java/java/"

# put extension of the file that will be compared

# used these extensions to compare files in c directory
# extension = ["c", "cpp", "h", "cc"]


# used these extensions to compare files in go directory
extension = ["java"]

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
    # used to compare files in c directory
#     call(["C:\Users\User\Desktop\sim_exe_3_0_2\sim_c++.exe", "-p", "-a", "-R","-o","result.txt", coin1path, coin2path])

    # used to compare files in go directory
    call(["C:\Users\User\Desktop\sim_exe_3_0_2\sim_text.exe", "-p", "-a", "-R","-o","result.txt", coin1path, coin2path])

def handler(signum, frame):
    print "Forever is over!"
    raise Exception("end of time")

class myThread (threading.Thread):
   def __init__(self, coin1, coin2):
      threading.Thread.__init__(self)
      self.coin1 = coin1
      self.coin2 = coin2
   def run(self):
      compare(self.coin1, self.coin2)




if __name__ == '__main__':
#     directorypath = "C:\Users\User\Desktop\sim_exe_3_0_2\coins/"
    coins = get_immediate_subdirectories(directorypath)
    
#     for root, dirs, files in os.walk(directorypath):
# #         print(root)
#         print(dirs)
# #         print(files)

    combi = rSubset(coins, r)
    
    count = 0
    threads =[]
    newcombi = []
    
#     # do not consider empty directory or directories that are too big
#     for thiscombi in combi:
#         coin1 = thiscombi[0]
#         coin2 = thiscombi[1]
#         coin1path = directorypath+ coin1
#         coin2path = directorypath + coin2 
#         
#         # get the size of directory
#         total_size1 = 0
#         for path, dirs, files in os.walk(coin1path):
#             for f in files:
#                 fp = os.path.join(path, f)
#                 total_size1 += os.path.getsize(fp)
#         
#         if ((total_size1 == 0) or (total_size1 > 10000000 )):
#             continue
#         
#         # get the size of directory
#         total_size2 = 0
#         for path, dirs, files in os.walk(coin2path):
#             for f in files:
#                 fp = os.path.join(path, f)
#                 total_size2 += os.path.getsize(fp)
#         
#         if ((total_size2 == 0) or (total_size2 > 10000000 )):
#             continue
#         newcombi.append(thiscombi)
        
#         print(coin2path + " size = " + str(total_size))
    conditionmet = 0
    for thiscombi in combi:
#         compare(thiscombi[0], thiscombi[1])


#         if (conditionmet == 0):
#             if(not((thiscombi[0] == "xdn-project-fantomcoinwallet-archive-master") and (thiscombi[1] == "ZencashOfficial-blue-app-btc-archive-master"))):
#                 continue
#             else:
#                 conditionmet = 1
        
        
        
        coin1 = thiscombi[0]
        coin2 = thiscombi[1]
        coin1path = directorypath+ coin1
        coin2path = directorypath + coin2 
        
        # get the size of directory
        total_size1 = 0
        
        #
#         counter = 0 
#         for path, dirs, files in os.walk("C:\\Users\\User\\Desktop\\java\\java"):
#             for dir in dirs:
#                 for path2, dirs2, files2 in os.walk(os.path.join("C:\\Users\\User\\Desktop\\java\\java",dir)):
#                     for f in files2:
#                         temp = str(counter)
#                         temp = temp + ".java"
#                         os.rename(os.path.join(path2,f), os.path.join(path2,temp))
#                         counter = counter + 1
        #
        
        for path, dirs, files in os.walk(coin1path):
            for f in files:
                fp = os.path.join(path, f)
                total_size1 += os.path.getsize(fp)
        
        if ((total_size1 == 0) or (total_size1 > 10000000 )):
            continue
        
        # get the size of directory
        total_size2 = 0
        for path, dirs, files in os.walk(coin2path):
            for f in files:
                fp = os.path.join(path, f)
                total_size2 += os.path.getsize(fp)
        
        if ((total_size2 == 0) or (total_size2 > 10000000 )):
            continue
        
#         thethread = myThread(thiscombi[0], thiscombi[1])
#         thethread.start()
        
        
        p = multiprocessing.Process(target=compare, args=(thiscombi[0],thiscombi[1]))
        threads.append(p)
        count = count + 1
        if (count == 10):
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            count = 0
            threads = []
#         p.start()
#          
#         count = count +1
#         if (count == 40):
#             break
#         
        
        
#         pid = subprocess.Popen([sys.executable, "compare(thiscombi[0], thiscombi[1])"]) # call subprocess
       
        
#         pid = subprocess.call(["compare", thiscombi[0],thiscombi[1]]) # call subprocess

#         DETACHED_PROCESS = 0x00000008
#         cmd = [
#                 sys.executable,
#                 'compare',
#                 thiscombi[0],
#                 thiscombi[1]
#               ]
#         p = subprocess.Popen(cmd,shell=False,stdin=None,stdout=None,stderr=None,close_fds=True,creationflags=DETACHED_PROCESS)
#         time.sleep(1000)
#         break

#             if (ismet == 0):
#                 if(not ((thiscombi[0] == "AElfProject-aelf-asset-chain-archive-master"))):
#                     ismet = 1
#                     continue




            