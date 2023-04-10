#! /usr/bin/env python3

# import modules - always before the code (at the top)
import argparse

# create ArgumentParser object - description calls for an output when help is called
parser = argparse.ArgumentParser(description='This script is to execute a FASTA file')

# add positional (required) arguments; when running the ./file -h the -h will display this message saying how the argument was positioned

# add positional arguments
parser.add_argument('GFF_name', help = 'The name of GFF file', type= str)
parser.add_argument('FASTA_filename', help = 'The name of FASTA file', type= str)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args()

# What I really need here:

file = covid.gff3

open(file)

file.readlines

close(file)

