# Run Ctest
The module is used to run the ctest against Cassandra 4.0.

## Prerequisites
- Java 11
- Ant 1.10.7

## How to set up cassandra
Using bash script:
- run, `./setup_cassandra.sh`
- check setup, `cd app/cassandra && CASSANDRA_USE_JDK11=true ant testsome -Dtest.name=org.apache.cassandra.hints.HintsCatalogTest -Dtest.methods=deleteHintsTest`

Or, set up manually:
- clone cassandra, `git clone https://github.com/apache/cassandra.git app/cassandra && cd app/cassandra`
- checkout commit, `git checkout 4e1d31e`
- apply injection patch, `git apply ../../ctest-injection.patch`
- build the project, `CASSANDRA_USE_JDK11=true ant`
- check setup, `CASSANDRA_USE_JDK11=true ant testsome -Dtest.name=org.apache.cassandra.hints.HintsCatalogTest -Dtest.methods=deleteHintsTest`

## How to run ctest
Run single test with modified configuration value:

`python run_single_ctest.py TESTNAME MODIFIEDCONF`

Example command:

`python run_single_ctest.py org.apache.cassandra.hints.HintsCatalogTest#deleteHintsTest storage_port=8080`