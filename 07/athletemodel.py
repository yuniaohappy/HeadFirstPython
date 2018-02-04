import pickle
import athletelist

def put_to_store(file_list):
    all_athlete = []
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athlete[ath.name] = ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athlete,athf)
    except IOError as ioe:
        print('File Error: ' + str(ioe))
        return None
def get_from_store():
    all_athlete = []
    try:
        with open('athletes.pickle','rb') as athf:
            all_athlete = pickle.load(athf)
    except IOError as ioe:
        print('File Error: ' + str(ioe))
    return(all_athlete)
