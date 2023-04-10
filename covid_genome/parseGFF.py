#! /usr/bin/env python3

# import modules - always before the code (at the top)
import argparse

# create ArgumentParser object - description calls for an output when help is called
parser = argparse.ArgumentParser(description='This script parses a GFF file')

# add positional (required) arguments; when running the ./file -h the -h will display this message saying how the argument was positioned

# add positional arguments
parser.add_argument('gff', help = 'The name of GFF file to parse', type= str)
parser.add_argument('fasta', help = 'The name of FASTA file to parse', type= str)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args()

# What I really need here 

#Read the gff file):
with open(args.gff) as x:
	for line in x: # loop over all the lines in the file
		print(line)
	
