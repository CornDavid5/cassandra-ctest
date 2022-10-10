def get_conf_params():
    config = []
    with open('../cassandra/conf/cassandra.yaml', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or len(line) == 0:
                continue
            comp = line.split(':')
            config.append(comp[0] + '\n')

    with open('conf_params.txt', 'w') as f:
        f.writelines(config)


# you may want to manually remove some configs which take multilevel value
# for example:
# audit_logging_options:
#     enabled: false
#     logger:
#       - class_name: BinAuditLogger
if __name__ == '__main__':
    get_conf_params()
