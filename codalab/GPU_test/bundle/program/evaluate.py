# Main program
# Test if GPU can be found and run a simple sript

# Imports
import sys
import os
import torch

# Run nvidia-smi command to check if the GPU is working
os.system('nvidia-smi')

# Paths
input_dir = sys.argv[1]
output_dir = sys.argv[2]
submit_dir = os.path.join(input_dir, 'res')
truth_dir = os.path.join(input_dir, 'ref')

# The submission
print('Initialize the submission')
sys.path.append(submit_dir)
from submission import Model
model = Model() # <--- torch.cuda.is_available() run here

if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Output file
    output_file = open(os.path.join(output_dir, 'scores.txt'), 'w')
    # Check GPU using PyTorch
    passing = model.is_gpu_available()
    output_file.write("passed: {}".format(int(passing)))
    output_file.close()

print('End of program')
