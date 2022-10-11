from glob import glob
import json


def get_test_method_list():
    path = r'../app/cassandra/test/unit/org/apache/cassandra/**/*Test.java'
    files = glob(path, recursive=True)
    test_method = []

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            package_name, class_name = '', ''
            line_num, length = 0, len(lines)

            for i in range(line_num, length):
                line_num = i
                if lines[i].startswith('package'):
                    package_name = lines[i].split()[-1][:-1]
                    break
            line_num += 1

            for i in range(line_num, length):
                line_num = i
                if lines[i].startswith('public class'):
                    class_name = lines[i].split()[2]
                    break
            line_num += 1

            prefix = package_name + '.' + class_name + '#'
            while line_num < length:
                if lines[line_num].strip().startswith('@Test'):
                    line_num += 1
                    comp = lines[line_num].split()
                    for c in comp:
                        i = c.find('(')
                        if i != -1:
                            test_method.append(prefix + c[:i])
                            break
                line_num += 1

    json_str = json.dumps(test_method)

    with open('test_method_list.json', 'w') as f:
        f.write(json_str)


if __name__ == '__main__':
    get_test_method_list()