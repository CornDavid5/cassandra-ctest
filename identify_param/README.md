# Identify Parameters
The module is used to generate the pair of configuration parameters and test methods.

## Prerequisites
- Java 11
- Ant 1.10.7
- Cassandra 4.0

## How to generate required files
We provide two python scripts to generate required files:
- `get_conf_params.py` will generate a list of configuration parameters used by cassandra.
- `get_test_method_list.py` will generate a list of test methods used by cassandra.

You need to put all generated files into the `results/cassandra` directory.

## How to set up cassadra
Using bash script:
- run, `./setup_cassandra.sh`
- check setup, `cd ../app/cassandra && CASSANDRA_USE_JDK11=true ant testsome -Dtest.name=org.apache.cassandra.service.GCInspectorTest -Dtest.methods=ensureStaticFieldsHydrateFromConfig`

Or, set up manually:
- clone cassandra, `git clone https://github.com/apache/cassandra.git ../app/cassandra && cd ../app/cassandra`
- checkout commit, `git checkout 4e1d31e`
- apply logging patches, `git apply ../../ctest-logging.patch`
- build the project, `CASSANDRA_USE_JDK11=true ant`
- check setup, `CASSANDRA_USE_JDK11=true ant testsome -Dtest.name=org.apache.cassandra.service.GCInspectorTest -Dtest.methods=ensureStaticFieldsHydrateFromConfig`

## How to gernerate parameter mapping
Using bash script:
- run, `./identify_param.sh`

Or, generate manually:
- to identify parameters, `python3 runner.py cassandra`
- to generate mapping based on identified parameters, `python3 collector.py cassandra`

## Note
- default config, [link](https://cassandra.apache.org/doc/latest/cassandra/getting_started/configuring.html)
- run test, [link](https://cassandra.apache.org/_/development/testing.html)
- the test report is in `/build/test/output`
- error `java.lang.UnsatisfiedLinkError: no netty_transport_native_epoll_x86_64 in java.library.path` may be ignored, [detail](https://stackoverflow.com/a/62219986)

## Challenges
- Cassandra uses ant to manage the project, therefore, need to modify the given python scripts to run the record the test results in Cassandra.
- Cassandra doesn't have an uniform get and set API, all get and set methods for each individual config are defined in the `DatabaseDescriptor.java` file, which is a pain to add all the logging.
