# To be submitted as a zip file containing:
# - submission.py (this file)
# - metadata file

# To understand how this code submission is executed, refer to:
# https://github.com/codalab/codalab-competitions/wiki/User_Building-an-Ingestion-Program-for-a-Competition#execution-priority

# Import
import torch
import os
import sys

if __name__=="__main__":
    # Paths
    input_dir = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])
    print("Using input_dir: " + input_dir)
    print("Using output_dir: " + output_dir)
    # True or False if GPU available or not
    gpu_available = torch.cuda.is_available()
    print('torch.cuda.is_available() --> {}'.format(gpu_available))
    # Write test result
    with open(os.path.join(output_dir, 'answer.txt'), 'w') as result_file:
        result_file.write(str(int(gpu_available)))
