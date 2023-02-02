## Compute Pi competition

This is a very simple example of competition with code submission, not using an ingestion program. For examples using an ingestion program, see [Yellow world](https://github.com/codalab/competition-examples/tree/master/codalab/Yellow_world) or [Iris](https://github.com/codalab/competition-examples/tree/master/codalab/Iris). The participants must submit a function that computes pi and the result is compared to a standard.
* [View the competition bundle](https://github.com/codalab/competition-examples/tree/master/codalab/Compute_pi/compute_pi_competition_bundle)
* [Download the competition bundle](https://github.com/codalab/competition-examples/blob/master/codalab/Compute_pi/compute_pi_competition_bundle.zip)
* [Download the sample submission](https://github.com/codalab/competition-examples/blob/master/codalab/Compute_pi/compute_pi_sample_submission.zip)

The competition has **3 phases**:
1. Development.
1. Feed-back.
1. Final test.

It features examples of uses of attributes of the YAML that are new to v1.5, which allow showing downloadable data and sample submission in the Files tab of the "Participate" section:
* `public_data`
* `starting_kit`

The competition bundle contains the following files:
```
dataset.zip	            The input data (to code submitted by participants)    
reference.zip               The solution to the problem
program.zip	            The program evaluating the solution
submission.zip	            A sample code submission
logo.jpg                    The logo
competition.yaml            The YAML configuration file
data.html	            HTML documentation pages	
evaluation.html		
overview.html	
terms_and_conditions.html
```

The [YAML file is the configuration file](https://github.com/codalab/competition-examples/blob/master/basic-competition-bundles/Compute_pi/compute_pi_competition_bundle/competition.yaml). It consist in a number of `attribute: value` pairs. For a full list of attributes, see the [Codalab competition YAML definition language](Organizer_Codalab-competition-YAML-definition-language).

1. **First section**: general settings and HTML pages
```
title: Example Competition
description: This is a competition to test the competition bundle system. It should be able to create a competition from this bundle.
image: logo.jpg
has_registration: True
end_date: 
html: 
    overview: overview.html
    evaluation: evaluation.html
    terms: terms_and_conditions.html
    data: data.html
```
2. **Second section**: phases (3 phases in this example)
```
phases:
    1:
        phasenumber: 1
        label: "Development"
        start_date: 2013-06-30
        max_submissions: 100
        is_scoring_only: False
        scoring_program: program.zip
        reference_data: reference.zip
        public_data: dataset.zip
        starting_kit: submission.zip
    2:
        phasenumber: 2
        label: "Feed-back"
        start_date: 2013-08-30
        max_submissions: 3
        is_scoring_only: False
        scoring_program: program.zip
        reference_data: reference.zip
        input_data: dataset.zip
    3:
        phasenumber: 3
        label: "Final test"
        start_date: 2013-09-30
        max_submissions: 3
        is_scoring_only: False
        scoring_program: program.zip
        reference_data: reference.zip
        input_data: dataset.zip
```
3. **Third section**: leaderboard configuration
```
leaderboard:
    leaderboards:
        Results: &RESULTS
            label: Results
            rank: 1
    columns:
        Difference:
            leaderboard: *RESULTS
            label: Difference
            numeric_format: 6
```
In this case, the scoring program writes a file `scores.txt` containing:
```
Difference:0
```
for the sample code submission.

### Types of data
We have used a zipfile `dataset.zip` as place holder for possible `public-data` or `input_data` that the code of the participants could use (though for this example this is no needed).
* **Public data**: Data provided for practice purposes, available for download during the development phase.
* **Input data:** Data fed to the participants' code but the does not leave the platform. Different data can be provided for the feed-back phase and the final test phase.

We also provide:
* **Reference data**: `reference.zip` is the solution to the problem.

### Building a scoring program

This example uses Python 2.7.

`evaluate.py` - is an example that checks that computes the difference between the estimation of pi computed by the code submission and the reference value.

`metadata` - a file that instruct Codalab to execute the scoring program.

Once these pieces are assembled they are packaged as program.zip which CodaLab can then use to evaluate the submissions for a competition.

### Sample code submission

This example uses Python 2.7.

`compute_pi.py` - provides examples of 3 algorithms that compute an approximation of pi.

`metadata` - instruct Codalab to execute the code:
```
command: python $program/compute_pi.py $input $output
```

This example does not use an organizer-provided ingestion program. For examples using an ingestion program, see [Yellow World](Example_yellow_world) and [Iris](Example_iris).

### Turning off code submission

You can easily change a code submission competition into a result submission competition:
* In the YAML file, change to `is_scoring_only: False`, or
* In the editor, check the box:

[-] Results Scoring Only

If code submission is enabled, participants may also submit results. All they need to do is to provide properly formatted results similar to the output of their code and submit a zipfile containing them, without `metadata` file. This of course can be done only if the participants can download the input data (e.g. in the development phase when the input data is provided as "public data").
