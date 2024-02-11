f = open("file.txt", "r")
nf = open("newfile.txt", "w")
nfl = []
for x in f:
  print(x)
  nfl.append(x)

nfl.sort()
for x in nfl:
  nf.write(x)

f.close()
nf.close()