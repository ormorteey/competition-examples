import sys
import subprocess
import os, os.path
from glob import glob
from sklearn.metrics import accuracy_score

def pip_install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print(f'Done installing {package}')

def get_label(filename):
    with open(filename, "r") as csvfile:
        read_arr = csvfile.readlines()
        label = [text.split(',')[0] for text in read_arr]
    return(label)

def score_fn(submission_file_name, truth_file_name):

    test_label = get_label(truth_file_name)
    submitted_list = get_label(submission_file_name)
    if len(test_label) != len(submitted_list):
        raise ValueError(f'Number of expected labels for does not match.\nExpected {len(test_label)-1} but {len(submitted_list)-1} was provided')
    if submitted_list[0] != 'label':
        raise ValueError('Submission file does not have a label column')
    else:
        submitted_list = submitted_list[1:]
        test_label = test_label[1:]
    acc = accuracy(true_label=test_label, pred_label=submitted_list)
    return acc


def accuracy(true_label, pred_label):
    return(sum(1 for x,y in zip(true_label,pred_label) if x == y) / float(len(true_label)))

# =============================== MAIN ========================================

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    print(f"input_dir: {input_dir}")
    print(f"output_dir: {output_dir}")
    
    directory =  os.getcwd()
    print(f"Current working directory: {directory}")
    print(f'Files in current working directory: {os.listdir(directory)}')

    truth_dir = os.path.join(input_dir, 'ref')

    if not os.path.isdir(truth_dir):
        print(f"{truth_dir} doesn't exist")
    else:
        print(f"{truth_dir} exists")
        print(f'Files in truth_dir ({truth_dir}): {os.listdir(truth_dir)}')

    submit_dir = os.path.join(input_dir, 'res')

    if not os.path.isdir(submit_dir):
        print(f"{submit_dir} doesn't exist")
    else:
        print(f"{submit_dir} exists")
        print(f'Files in submit_dir ({submit_dir}): {os.listdir(submit_dir)}')

    glob_submit_files = glob(os.path.join(submit_dir, '*.csv'), recursive=True)
    print(f'glob_submit_files: {glob_submit_files}')

    glob_truth_files = glob(os.path.join(truth_dir, '*.csv'), recursive=True)
    print(f'glob_truth_files: {glob_truth_files}')

    truth_file = os.path.join(truth_dir, 'mnist_test.csv')
    submit_file = os.listdir(submit_dir)[0]
    submission_file = os.path.join(submit_dir, 'mnist_test.csv')


    if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created {output_dir}")

        output_filename = os.path.join(output_dir, 'scores.txt')              
        output_file = open(output_filename, 'w')
        print(f"Starting scoring of submission_file: {submission_file}")
        accuracy = score_fn(submission_file, truth_file)
        # accuracy = score_fn(truth_file, truth_file)
        print(f"Accuracy: {accuracy}")
        output_file.write(f"Accuracy:{accuracy}")
        output_file.close()