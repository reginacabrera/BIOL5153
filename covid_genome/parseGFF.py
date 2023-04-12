#! /usr/bin/env python3

# import modules - always before the code (at the top)
import argparse

# create ArgumentParser object - description calls for an output when help is called
parser = argparse.ArgumentParser(description='This script parses a GFF file')

# add positional (required) arguments; when running the ./file -h the -h will display this message saying how the argument was positioned

# add positional arguments
parser.add_argument('gff_file', help = 'The name of GFF file to parse', type= str)
parser.add_argument('fasta', help = 'The name of FASTA file to parse', type= str)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args()
	
#reading the file
GFF_file = open(args.gff_file, 'r')
GFF_lines = GFF_file.readlines()
GFF_file.close()
GFF_lines.remove(GFF_lines[-1])

# GFF_lines2 = []
for line in GFF_lines:
    stripped_line = line.strip()
    stripped_line2 = stripped_line.split('\t')
    length = (int(stripped_line2[4]) - int(stripped_line2[3]) + 1)
    print(stripped_line2[2] + '\t' + str(length))
    
    
    