## GPU test bundle

This is a very simple bundle with code submission, not using an ingestion program. For examples using an ingestion program, see [Yellow world](https://github.com/codalab/competition-examples/tree/master/codalab/Yellow_world) or [Iris](https://github.com/codalab/competition-examples/tree/master/codalab/Iris). The goal of this bundle is simply to test a queue of GPU compute workers, checking that everything is working fine.
* [View the bundle](bundle/)
* [Download the bundle](bundle.zip)
* [Download the test submission](submission.zip)

#### Queue and docker

* This bundle uses the following Docker image: `codalab/codalab-legacy:gpu`
* You need to set manually the queue to a queue containing GPU workers

#### Make bundle

```
cd bundle/utilities
./make_bundle.sh
```
