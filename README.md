## Prerequisites
- Java 11
- Ant 1.10.7
- Cassandra 4.0

## How to set up for generate parameters mapping
- clone cassandra, `git clone https://github.com/apache/cassandra.git app/cassandra && cd app/cassandra`
- checkout commit, `git switch cassandra-4.0`
- apply logging patches, `git apply ../../ctest-logging.patch`
- build the project, `CASSANDRA_USE_JDK11=true ant`
- example test command, `CASSANDRA_USE_JDK11=true ant testsome -Dtest.name=org.apache.cassandra.config.YamlConfigurationLoaderTest`

## Note
- default config, [link](https://cassandra.apache.org/doc/latest/cassandra/getting_started/configuring.html)
- run test, [link](https://cassandra.apache.org/_/development/testing.html)
- the test report in in `/build/test/output`

## Challenges
- Cassandra uses ant to manage the project, therefore, its testing result structure is different from maven surefire.
- It does not usually have a get API, all get operation is done directly via reading the Config class's public fields.