import os
myfile = open(".\TWR.txt", "r")
dest = open(".\TWR_CONV.txt", "w")
for line in myfile:
    coord = line.split(" ")
    
    north = coord[0].split(".")
    nd=north[0]
    nm=north[1]
    ns=north[2]
    
    east = coord[1].split(".")
    ed=east[0]
    em=east[1]
    es=east[2]
    
    north1 = coord[2].split(".")
    nd1=north1[0]
    nm1=north1[1]
    ns1=north1[2]

    east1 = coord[3].split(".")
    ed1=east1[0]
    em1=east1[1]
    es1=east1[2]

    dest.write("[\""+nd+"d"+nm+"m"+ns+"\", \""+ed+"d"+em+"m"+es+"\", \""+nd1+"d"+nm1+"m"+ns1+"\", \""+ed1+"d"+em1+"m"+es1+"\"],\n")

print("Done!")