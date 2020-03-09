import os
myfile = open("Desktop\\fixes.txt", "r")
dest = open("Desktop\\fixed_fixes.txt", "w")
for line in myfile:
    splits = line.split(" ")
    fix_name = splits[0]
    nd = splits[1]
    nm = splits[2]
    ns = splits[3]+"."+splits[4]
    ed = splits[5]
    em = splits[6]
    es = splits[7]+"."+splits[8].split("\n")[0]
    dest.write("\""+fix_name+"\""+": [\""+nd+"d"+nm+"m"+ns+"\", \""+ed+"d"+em+"m"+es+"\"],"+"\n")
