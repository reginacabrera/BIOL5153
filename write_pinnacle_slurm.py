#! /usr/bin/env python3

# import modules - always before the code (at the top)
import argparse

# create ArgumentParser object - description calls for an output when help is called
parser = argparse.ArgumentParser(description='This script returns a SLURM script with options fro the AHPCC cluster')

# add positional (required) arguments; when running the ./file -h the -h will display this message saying how the argument was positioned

# add positional arguments
parser.add_argument('job_name', help = 'The name of the SLURM job', type= str)

# add optional arguments
# the default for 'store_true' is ... "False"
# if 'store_true', then assign 'True' with -v or --verbose; the - (dash) is the difference between the optional and the require arguments, and double -- before the variable name
parser.add_argument('-q', '--queue', help = 'Which queue to utilize (comp01, comp06, comp72)', default = 'comp72', type= str)
parser.add_argument('-n', '--num_nodes', help = 'Number of nodes to utilize', default = '1', type= int)
parser.add_argument('-p', '--num_processors', help = 'Number of processors to utilize', default = '24', type= int)
parser.add_argument('-w', '--walltime', help = 'Estimated time for the job to be processed', default = '72', type= int)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args()

# What I really need here:

# print bash header
print('#!/bin/bash')

print()

# print SBATCH commands
print('#SBATCH --job-name=' + args.job_name)
print('#SBATCH --partition', args.queue)
print('#SBATCH --nodes=' + str(args.num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(args.num_processors))
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
print('#SBATCH -o arcabrer_%j.out')
print('#SBATCH -e arcabrer_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=arcabrer@uark.edu')


print()

# purge all the modules
print('module purge')

print()

# cd into the submit directory
print('cd $SLURM_SUBMIT_DIR')

print()

print('# job command here')