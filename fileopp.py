import collections
import datetime

def loadfile(inputFile):
  if inputFile is not None :
    output = collections.defaultdict(int)
    with open( inputFile, 'r' ) as fp :
      lines = fp.read().replace('\r', '' ).split( '\n' )

    for ( index, line ) in enumerate( lines, start = 1 ) :
      line = line.strip()
      
      if (line and line[0] != "#") :
        lineData = line.split()
        if output[lineData[0]] != 0:
          output[lineData[0]] += 1
        else:
          output[lineData[0]] = 1
    # filename = "{0}.txt".format(str(datetime.datetime.now())) 
    f= open("filename1.txt","w+")
    for i in output:
     f.write("{0} {1}\r\n".format(i, output[i]))
    f.close()
  else:
    return False

loadfile("filename.txt")