## Prerequisites
- Java 11
- Ant 1.10.7
- Maven 3.6.3
- Python 3.8
- Cassandra 4.0

## How to set up for generate parameters mapping
- clone cassandra, `git clone https://github.com/apache/cassandra.git app/cassandra && cd app/cassandra`
- checkout commit, `git switch cassandra-4.0`
- apply logging patches, `git apply ../../ctest-logging.patch`
- build the project, `CASSANDRA_USE_JDK11=true ant`

## Note
- default config, [link](https://cassandra.apache.org/doc/latest/cassandra/getting_started/configuring.html)
- run test, [link](https://cassandra.apache.org/_/development/testing.html)
- the test report in in `/build/test/output`