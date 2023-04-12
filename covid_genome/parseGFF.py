#! /usr/bin/env python3

# import modules - always before the code (at the top)
import argparse
import csv

# create ArgumentParser object - description calls for an output when help is called
parser = argparse.ArgumentParser(description='This script parses a GFF file')

# add positional (required) arguments; when running the ./file -h the -h will display this message saying how the argument was positioned

# add positional arguments
parser.add_argument('gff_file', help = 'The name of GFF file to parse', type= str)
parser.add_argument('fasta', help = 'The name of FASTA file to parse', type= str)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args()


#WHAT I DID
#reading the file

#GFF_file = open(args.gff_file, 'r')
#GFF_lines = GFF_file.readlines()
#GFF_file.close()
#GFF_lines.remove(GFF_lines[-1])

# GFF_lines2 = []

#for line in GFF_lines:
 #   stripped_line = line.strip()
 #   stripped_line2 = stripped_line.split('\t')
 #   length = (int(stripped_line2[4]) - int(stripped_line2[3]) + 1)
 #   print(stripped_line2[2] + '\t' + str(length))
    
# ---- CLASS VERSION

#open the GFF file (with function automatically closes the file and the lines become a list)
with open (args.gff_file) as gff_file:

	# create a csv reader object
	reader = csv.reader(gff_file, delimiter = '\t')

	#loop over all the lines in the file
	for line in reader:
 			
 		#skip blank lines
 		if not line:
 			continue #this take us to the next line
 		
 		#else it's not a blank line
 		else: 	
 			#print(line)	
 			#line = line.strip() #remove the line breaks
 			#split line on tab character
 			#columns = line.split('\t')
			# print(line)
		
			#give variable names to the column
 			organism = line[0]
 			source = line[1]
 			feature_type = line[2]
 			start = int(line[3])
 			end = int(line[4])
 			length = line[5]
 			strand = line[6]
 			attributes = line[8]
 			
 			#add the length to column 5
 			line[5] = str(int(end) - int(start) + 1) 
 			
 			new_line = '\t'.join(line)

 			print(new_line)
 
 # ./nameofthefile.py gff3_file fasta_file | less -S (the less -S will show it organized by columns)		   
 		
 		
 		
 		
 		
 		
 		
 		
 		
 		
 		
 		
    