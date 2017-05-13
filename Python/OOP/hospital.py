import itertools # to keep count of each class created, which will in turn be used for the id

class Patient(object):

    _id = itertools.count(0)
    def __init__(self, name, allergies):
        self.id = self._id.next() # assign a unique id to each class created
        self.name = name
        self.allergies = allergies
        self.bed_number = None # no bed assignment until admitted into a hospital

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name #name of hospital
        self.capacity = [] # this will contain the number of beds in a hospital
        for each in range(0, capacity):
            self.capacity.append(each + 1)

    def admit(self, patient):
        if len(self.capacity) > 0:
            self.patients.append(patient)
            patient.bed_number = self.capacity.pop()
            print 'Welcome to', self.name, 'your bed number is', patient.bed_number
        elif len(self.capacity) == 0:
            print 'Sorry we are at capacity and cannot receive new patients.'
        return self

    def discharge(self, patient):
        try:
            self.patients.remove(patient)
            self.capacity.append(patient.bed_number)
            print 'Goodbye', patient.name, "stay healthy."
        except ValueError:
            print 'There is no patient here by the name', patient.name, 'please enter a differnet patient name.'
        return self

    def show_info(self):
        print '-'*20
        print 'Hospital:', self.name
        print 'Current patients:'
        for each in self.patients:
            print each.name, 'in bed', each.bed_number
        print 'Current open beds:', len(self.capacity)
        print '-'*20
        return self


patient1 = Patient('Qtip', 'bad rhymes')
patient2 = Patient('Phife Dog', 'bad vibes')
patient3 = Patient('Ali Shaheed Muhammad', 'bad beats')

hospital1 = Hospital('A Tribe Called Quest', 4)

hospital1.admit(patient3).admit(patient2).show_info().discharge(patient2).show_info()
