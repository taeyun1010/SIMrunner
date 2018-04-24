from subprocess import call
# Function which returns subset or r length from n
from itertools import combinations

coins = ["bitcoin", "BTCGPU", "rippled"]
r = 2

def rSubset(arr, r):
 
    # return list of all subsets of length r
    # to deal with duplicate subsets use 
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))

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
                        index = thisline.find("consists for")
                        index = index + 13
                        split = thisline[index:]
                        endindex = split.find("%") - 1
                        totalsum = totalsum + int(split[:endindex])
                        fo.write(thisline)
                print("Similarity percentage between " + thiscombi[0] + " and " + thiscombi[1] + " = " + str((totalsum / count)))