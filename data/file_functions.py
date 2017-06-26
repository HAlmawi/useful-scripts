#source: https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python

def get_num_lines(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
