import os

# change to the parent direcotry
directorypath = "C:\Users\User\Desktop\test_rm"

if __name__ == '__main__':
    for path, dirs, files in os.walk(directorypath):
        for dir in dirs:
            print(dir)
#             # get the size of directory
#             dirsize = 0
#             for path, dirs, files in os.walk(os.path.join(path,dir)):
#                 for f in files:
#                     fp = os.path.join(path, f)
#                     dirsize += os.path.getsize(fp)
#             print("size = " + str(dirsize))
# #                   os.rmdir(dir)
# 
# 
#             try:
#                 os.rmdir(os.path.join(path,dir))
#             except OSError as ex:
#                 print "error"
# #                 if ex.errno == errno.ENOTEMPTY:
# #                     print "directory not empty"