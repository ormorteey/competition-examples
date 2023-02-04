# Main program
# Test if GPU can be found and run a simple sript

# Imports
import sys
import os
import torch

# Run nvidia-smi command to check if the GPU is working
os.system('nvidia-smi')
print() # line break

# Paths
input_dir = sys.argv[1]
output_dir = sys.argv[2]
submit_dir = os.path.join(input_dir, 'res')
truth_dir = os.path.join(input_dir, 'ref')

if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Output file
    output_file = open(os.path.join(output_dir, 'scores.txt'), 'w')
    # Check GPU using PyTorch (output of the submission)
    print('Reading the result of the test (from the submission)')
    test_result_file = os.path.join(submit_dir, 'answer.txt')
    if os.path.exists(test_result_file):
        f = open(test_result_file, 'r')
        gpu_available = int(f.read())
        f.close()
    # Write score for leaderboard
    result = "gpu_available: {}".format(gpu_available)
    print(result)
    output_file.write(result)
    output_file.close()
print('End of program')
