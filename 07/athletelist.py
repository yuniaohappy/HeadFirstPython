class AthleteList(list):
    def __init__(self,a_name,a_dob = None,a_times = []):
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return()