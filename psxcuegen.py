#!/usr/bin/python

import os
from os import walk
from os.path import splitext
import sys

def create_psx_cue(bin_name):
    try:
	cue = open(bin_name+'.cue', 'w')
	text = 'FILE \"' + bin_name + '.bin\" BINARY\n'
	text += ' TRACK 01 MODE2/2352\n'
	text += '  INDEX 01 00:00:00\n'
	text += ' POSTGAP 00:02:00\n'
	cue.write(text)
        cue.close()
        print "Successfully wrote " + bin_name + '.cue'
    except:
        print >> sys.stderr, 'Unable to write file: ' + bin_name + '.cue'

def main():
    cwd = os.getcwd()
    
    files = []
    for (dirpath, dirnames, filenames) in walk(cwd):
        files.extend(filenames)
        break
    
    bins = []
    cues = []

    for file in files:
        f_name = splitext(file)[0].split('.')[0]
        try:
            ext = splitext(file)[1].split('.')[1]
        except:
            pass
        if ext is not None:
            if ext.lower() == 'bin':
                bins.append(f_name)
            elif ext.lower() == 'cue':
                cues.append(f_name)
    
    
    # verify that for each bin, there is a corresponding cue

    bins_without_cues = []

    for b in bins:
        if b not in cues:
            bins_without_cues.append(b)

    for bwc in bins_without_cues:
    	create_psx_cue(bwc)


if __name__ == '__main__':
	main()
