def from_file_to_list():
    l = []
    with open('a.txt', 'r') as f:
        line = f.readline()
        while line:
            l.append(line)
            line = f.readline()
    return l

def del_slash_n(l):
    for i in range(len(l)):
        l[i] = l[i][:-1]
    return l

def _split_(l):
    for i in range(len(l)):
        l[i] = l[i].split(',')
        for j in range(len(l[i])):
            l[i][j] = [l[i][j]]
    return l

def add_keys(l):
    l2 = ['name', 'surname', 'birth', 'prof']
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j].insert(0, l2[j])
    return l

def to_dict(l):
    for i in range(len(l)):
        l[i] = dict(l[i])
    return l

def to_new_file(l):
    with open('b.txt', 'w') as f:
        f.write(str(l))
    return f

print(to_dict(add_keys(_split_(del_slash_n(from_file_to_list())))))
to_new_file(to_dict(add_keys(_split_(del_slash_n(from_file_to_list())))))
