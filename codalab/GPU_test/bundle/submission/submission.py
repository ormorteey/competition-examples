# To be submitted as a zip file containing:
# - submission.py (this file)
# - metadata file

# Import
import torch

class Model:
    def __init__(self):
        # True or False if GPU available or not
        self.passing = torch.cuda.is_available()

    def is_gpu_available(self):
        return self.passing
