#import time
# ga ada Output

f = open("contoh.txt", "rt")

#rt = read text
#print(f.read())

#f.close()

#with open("contoh.txt", "rt") as f:
    #print(f.read(5))

    #print(f.readline())

   # for x in f:
  #      print(x)

  #  with open("contoh.txt", "a") as f:
 #       f.write("\nNIM : 25071101720")

#time.sleep(5) 

#with open("contoh.txt", "w") as f:
   # f.write("Ke overwrite")

#with open("file_baru.txt", "w") as f:
 #   pass

import os

if os.path.exists("file_baru.txt"):
    os.remove("file_baru.txt")
else:
    print("file_baru.txt tidak ada")


