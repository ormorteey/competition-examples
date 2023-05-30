# Iris Challenge Example

This is a very simple example of competition in 2 phases, with either result or code submission, using an ingestion program.
It allows organizers to write a program that received Python classes (not executables) and call them on data loaded with a standard data loader (ehnce the participants do not have to read the input data themselves).

The example uses the well known Iris dataset from Fisher's classic paper (Fisher, 1936).. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other.

* [View the competition bundle](https://github.com/codalab/competition-examples/tree/master/codalab/Iris/iris_competition_bundle)
* [Download the competition bundle](https://github.com/codalab/competition-examples/blob/master/codalab/Iris/iris_competition_bundle.zip)
* [Download the sample code submission](https://github.com/codalab/competition-examples/blob/master/codalab/Iris/iris_sample_code_submission.zip)
* [Download the sample result submission](https://github.com/codalab/competition-examples/blob/master/codalab/Iris/iris_sample_result_submission.zip)

### References and credits

R. A. Fisher. The use of multiple measurements in taxonomic problems. Annual Eugenics, 7, Part II, 179-188 (1936). 
The competition protocol was designed by Isabelle Guyon. 
This challenge was generated using ChaLab for Codalab v1.5.

### Overview

There are 2 phases:

* Phase 1: development phase. We provide you with labeled training data and unlabeled validation and test data. Make predictions for both datasets. However, you will receive feed-back on your performance on the validation set only. The performance of your LAST submission will be displayed on the leaderboard.

* Phase 2: final phase. You do not need to do anything. Your last submission of phase 1 will be automatically forwarded. Your performance on the test set will appear on the leaderboard when the organizers finish checking the submissions.

This sample competition allows you to submit either:

* Only prediction results (no code).
* A pre-trained prediction model.
* A prediction model that must be trained and tested.

NOTE: we provide the zipped and unzipped competition bundle for convenience. In the competition bundle, subdirectories should be zipped files (e.g scoring\_program). You can use the `make_competition_bundle.sh` script for that purpose:

```
cd iris_competition_bundle/utilities
./make_competition_bundle.sh
```

You can try your newly created competition by submitting one of those files into it:
```
sample_result_submission.zip
sample_code_submission.zip
```





It has a special workflow: submissions are made only during the first phase and they are automatically forwarded to the second phase:

![Iris_Tutorial](https://user-images.githubusercontent.com/11784999/216441257-19878303-fe95-4633-9323-c87dd7e0a620.png)


The competition bundle contains the following files:
```
input_data_1.zip	    The input data (to code submitted by participants); same for both phases    
reference_data_1.zip        The solution to the problem, in the 1st phase
reference_data_2.zip        The solution to the problem, in the 2nd phase
ingestion_program_1.zip     The ingestion program
scoring_program_1.zip	    The program evaluating the solution (same in both phases)
starting_kit_1.zip	    The starting kit to generate sample submissions
logo.png                    The logo
competition.yaml            The YAML configuration file
data.html	            HTML documentation pages	
evaluation.html		
overview.html	
terms.html
get_starting_kit.html
```

The [YAML file is the configuration file](https://github.com/codalab/competition-examples/blob/master/basic-competition-bundles/Iris/iris_competition_bundle/competition.yaml). It consist in a number of `attribute: value` pairs. For a full list of attributes, see the [Codalab competition YAML definition language](Organizer_Codalab-competition-YAML-definition-language).

1. **First section**: general settings and HTML pages
```
title: Iris
description: The well known Iris dataset from Fisher's classic paper (Fisher, 1936).
image: logo.png
has_registration: false
html:
  data: data.html
  evaluation: evaluation.html
  get_starting_kit: get_starting_kit.html
  overview: overview.html
  terms: terms.html
```
2. **Second section**: phases (3 phases in this example)
```
phases:
  0:
    color: green
    ingestion_program: ingestion_program_1.zip
    input_data: input_data_1.zip
    label: Development
    max_submissions: 100
    max_submissions_per_day: 5
    phasenumber: 1
    public_data: input_data_1.zip
    reference_data: reference_data_1.zip
    scoring_program: scoring_program_1.zip
    start_date: 2017-10-22 18:53:00+00:00
    starting_kit: starting_kit_1.zip
  1:
    color: purple
    ingestion_program: ingestion_program_1.zip
    input_data: input_data_1.zip
    label: Final
    max_submissions: 100
    max_submissions_per_day: 0
    phasenumber: 2
    reference_data: reference_data_2.zip
    scoring_program: scoring_program_1.zip
    start_date: 2018-04-30 18:53:00+00:00
```
3. **Third section**: leaderboard configuration
```
leaderboard:
  columns:
    Duration:
      label: Duration
      leaderboard: &id001
        label: Results
        rank: 1
      rank: 7
      sort: desc
    set1_score:               # This is the name of the score returned in score.txt written by the scoring program
      label: Prediction score # This will be the name of the column showing the results
      leaderboard: *id001
      rank: 2
      sort: desc              # Change that to "asc" if you want to sort the score in ascending order
  leaderboards:
    Results: *id001
```
In this case, the scoring program writes a file `scores.txt` containing:
```
set1_score: 0.5
Duration: 0.123
```

### Types of data
We have several zip files providing data:
* **Public data**: `input_data_1.zip` is provided to the participants for download in the first phase. 
* **Input data**: `input_data_1.zip` is also provided to the submitted code on the Codalab platform.  
* **Reference data**: `reference_data_1.zip` is the solution to the problem in the 1st phase (occluded to the participants). `reference_data_2.zip` is the solution to the problem in the 2nd phase.

### Ingestion program

This competition uses an [Ingestion Program](User_Building-an-Ingestion-Program-for-a-Competition). 

`ingestion.py` - In this example, datasets are loaded and a class `model.py` supplied by the participants is called to train and test a model.

`metadata` - instruct Codalab to execute the ingestion program when a participant submits code.

These pieces and other library functions are packaged as ingestion_program_1.zip to process the submissions for this competition.

### Sample code submission

`model.py` - is a class containing a predictive model with 2 methods: `fit` and `predict`. This is inspired by the interface of the scikit-learn Python library of machine learning.

`metadata` - instruct Codalab that this is a code submission. There is no command though because the code is not executable.
```
description: this is a non executable code submission.
```

For examples of code submissions that are executable and do not require an ingestion program, see [Yellow World](Example_yellow_world) and [Compute Pi](Example_compute-pi).

### Scoring program

`score.py` - is an example that computes the performance of prediction using the metric given in `metric.txt`.

`metadata` - this is the file that provides the command to run the scoring program.

These pieces and other library functions are packaged as scoring_program_1.zip to evaluate the predictions made by code submitted by the participants.

### Result submission

This competition also accepts result submissions. All the participants need to do is to provide properly formatted results (similar to the output of their code submission) and submit a zipfile containing them, without `metadata` file. This can be done since the participants can download the input data (which is the same as the public data).

You can easily turn this competition into a result submission ONLY competition:
* In the YAML file, change to `is_scoring_only: False`, or
* In the editor, check the box:

[-] Results Scoring Only

![logo](iris_competition_bundle/logo.png)