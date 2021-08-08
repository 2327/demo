counter = {}

def calculate_hits():
    with open('log', 'r', encoding='utf8') as log:
        for line in log:
            _ip = line.split(' ')[0]
            if _ip not in counter.keys():
                counter[_ip] = 1
            else:
                counter[_ip] += 1

    return counter

def print_top():
    for top in sorted(calculate_hits().values(),reverse=True)[:5]:
        for key, value in counter.items():
            if value == top:
                print(f'ip: {key} hits: {value}')

if __name__ == '__main__':
    print_top()

