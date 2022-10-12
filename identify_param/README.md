## Prerequisites
- Java 11
- Ant 1.10.7
- Cassandra 4.0

## How to set up cassadra
Using add_project script:
- run, `./add-project.sh cassandra`
- check setup, `cd app/cassandra && CASSANDRA_USE_JDK11=true ant testsome -Dtest.name=org.apache.cassandra.service.GCInspectorTest -Dtest.methods=ensureStaticFieldsHydrateFromConfig`

Or, set up manually:
- clone cassandra, `git clone https://github.com/apache/cassandra.git app/cassandra && cd app/cassandra`
- checkout commit, `git switch cassandra-4.0`
- apply logging patches, `git apply ../../ctest-logging.patch`
- build the project, `CASSANDRA_USE_JDK11=true ant`
- check setup, `CASSANDRA_USE_JDK11=true ant testsome -Dtest.name=org.apache.cassandra.service.GCInspectorTest -Dtest.methods=ensureStaticFieldsHydrateFromConfig`

## How to gernerate parameter mapping
- to identify parameters, `python3 runner.py cassandra`
- to generate mapping based on identified parameters, `python3 collector.py`

## Note
- default config, [link](https://cassandra.apache.org/doc/latest/cassandra/getting_started/configuring.html)
- run test, [link](https://cassandra.apache.org/_/development/testing.html)
- the test report is in `/build/test/output`
- error `java.lang.UnsatisfiedLinkError: no netty_transport_native_epoll_x86_64 in java.library.path` may be ignored, [detail](https://stackoverflow.com/a/62219986)

## Challenges
- Cassandra uses ant to manage the project, therefore, need to modify the given python scripts to run the record the test results in Cassandra.
- Cassandra doesn't have an uniform get and set API, all get and set methods for each individual config are defined in the `DatabaseDescriptor.java` file, which is a pain to add all the logging.
