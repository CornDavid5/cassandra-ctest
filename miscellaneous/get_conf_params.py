def get_conf_params():
    config = []
    with open('../app/cassandra/src/java/org/apache/cassandra/config/Config.java', 'r') as f:
        lines = f.readlines()

        for i in range(52, 585):
            line = lines[i].strip()

            if not line.startswith('public') or not line.endswith(';'):
                continue

            eq_i = line.find('=')
            if eq_i == -1:
                comp = line.split()
                config.append(comp[-1][:-1] + '\n')
            else:
                comp = line[:eq_i].split()
                config.append(comp[-1].strip() + '\n')

    with open('conf_params.txt', 'w') as f:
        f.writelines(config)


if __name__ == '__main__':
    get_conf_params()
