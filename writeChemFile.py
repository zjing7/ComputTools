#!/usr/bin/env python

def writeTXYZ(outXYZ, order, atoms, coord, types, connections):
	fout = open(outXYZ, "w")
	fout.write("%3s #Generated by chemFileConvert.py\n"%len(atoms))
	for n in range(len(atoms)):
	  if len(connections[n])==0:
	    fout.write("%6s%3s%14.7f%14.7f%14.7f%6s\n"%(order[n],atoms[n],float(coord[n][0]),float(coord[n][1]),float(coord[n][2]), types[n]))
	  if len(connections[n])==1:
	    fout.write("%6s%3s%14.7f%14.7f%14.7f%6s%3s\n"%(order[n],atoms[n],float(coord[n][0]),float(coord[n][1]),float(coord[n][2]), types[n], connections[n][0]))
	  if len(connections[n])==2:
	    fout.write("%6s%3s%14.7f%14.7f%14.7f%6s%3s%3s\n"%(order[n],atoms[n],float(coord[n][0]),float(coord[n][1]),float(coord[n][2]), types[n], connections[n][0], connections[n][1]))
	  if len(connections[n])==3:
	    fout.write("%6s%3s%14.7f%14.7f%14.7f%6s%3s%3s%3s\n"%(order[n],atoms[n],float(coord[n][0]),float(coord[n][1]),float(coord[n][2]), types[n], connections[n][0], connections[n][1], connections[n][2]))
	  if len(connections[n])==4:
	    fout.write("%6s%3s%14.7f%14.7f%14.7f%6s%3s%3s%3s%3s\n"%(order[n],atoms[n],float(coord[n][0]),float(coord[n][1]),float(coord[n][2]), types[n], connections[n][0], connections[n][1], connections[n][2], connections[n][3]))
	fout.close()
