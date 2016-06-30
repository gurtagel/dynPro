x = raw_input("Enter a filename: ").strip("\r\n")
biglist = []
tmplist = []
f = open(x, "r")
i = 0

for lines in f:
   if i == 1:
      rows = int(lines)
   elif i == 0:
      cols = int(lines)
   else:
      intlist = lines.split()
      for thing in intlist:
         tmplist.append(int(thing))
      biglist.append(tmplist)
      tmplist = []
   i += 1

tracker = [[0 for i in xrange(rows)] for i in xrange(cols)]

for i in range(len(biglist)):
   for j in range(len(biglist[i])):
      if i == 0 and j == 0:
         tracker[0][0] = 0
      elif i == 0:
         if biglist[i][j-1] + biglist[i][j] > biglist[i][j]:
            biglist[i][j] = biglist[i][j-1]+biglist[i][j]

            tracker[i][j] = -1
         else:
            tracker[i][j] = 0
      elif j == 0:
         if biglist[i-1][j] + biglist[i][j] > biglist[i][j]:
            biglist[i][j] = biglist[i-1][j]+biglist[i][j]
            tracker[i][j] = 1
         else:
            tracker[i][j] = 0
      else:
         if biglist[i-1][j] + biglist[i][j] > biglist[i][j] or biglist[i][j-1] + biglist[i][j] > biglist[i][j]:
            if biglist[i-1][j] + biglist[i][j] > biglist[i][j-1] + biglist[i][j]:
               tracker[i][j] = 1
               biglist[i][j] = biglist[i-1][j]+biglist[i][j]
            else:
               tracker[i][j] = -1
               biglist[i][j] = biglist[i][j-1]+biglist[i][j]
         else:
            tracker[i][j] = 0

max = -100000000000000
bestin = []
for i in range(len(biglist)):
   for j in range(len(biglist[i])):
      if (i == len(biglist) - 1 or j == len(biglist[i]) - 1) and biglist[i][j] > max:
         max = biglist[i][j]
         bestin = [i,j]
print "Best Solution is: " + str(max)


curPath = []
curPath.append([bestin[1], bestin[0]])

curdat = tracker[bestin[0]][bestin[1]]
newi = bestin[0]
newj = bestin[1]
while (curdat != 0):
   if curdat == 1:
      curPath.insert(0, [newj, newi - 1])
      newi = newi - 1
      curdat = tracker[newi][newj]
   else:
      curPath.insert(0, [newj - 1, newi])
      newj = newj - 1
      curdat = tracker[newi][newj]


print "Here is the path"

#print str(curPath[i][0]) + " " +str(curPath[i][1])   



