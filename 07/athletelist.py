def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mi, secs) = time_string.split(splitter)
    return ( mi + '.' + secs)

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set(sanitize(s) for s in self))[0:3])


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(',')
            return(AthleteList(data.pop(0),data.pop(0),data))
    except IOError as ioe:
        print('File error: ' + ioe)
        return(None)
sarah = get_coach_data('sarah.txt')
print(sarah.name + '\t' + str(sarah.top3()))
