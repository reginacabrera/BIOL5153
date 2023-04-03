#! usr/bin/env python3

# import modules
import argparse

# create ArgumentParser object
parser = argparse.ArgumentParser(description='This script returns a SLURM script with options')

# add positional (required) arguments; when running the ./file -h the -h will display this message saying how the argument was positioned

# add positional arguments
parser.add_argument('job', help = 'The name of the SLURM job', type = str)

# add optional arguments
# the default for 'store_true' is ... "False"
# if 'store_true', then assign 'True' with -v or --verbose
parser.add_argument('-q', '-queue', help = 'Which queue to utilize', default = 'comp01', type = str)
parser.add_argument('-nodes', help = 'Number of nodes to utilize', default = 1, type = int)
parser.add_argument('-processors', help = 'Number of processors to utilize', default = 24, type = int)
parser.add_argument('-walltime', help = 'Estimated time for the job to be processed', default = 1, type = int)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args()

# What I really need here:

job_name = args.job
queue = args.q
walltime = args.nodes
num_nodes = args.processors
num_processors = args.walltime

# print bash header
print('#!/bin/bash')

print()

# print SBATCH commands
print('#SBATCH --job-name=' + job_name)
print('#SBATCH --partition', queue)
print('#SBATCH --nodes=' + str(num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(num_processors))
print('#SBATCH --time=' + str(walltime) + ':00:00')
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