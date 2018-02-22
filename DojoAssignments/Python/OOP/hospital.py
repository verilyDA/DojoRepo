class patient(object):
    uid = 0
    def __init__(self, name, allergies):
        patient.uid += 1
        self.id = patient.uid
        self.name = name
        self.allergies = allergies
        self.bed = 'none'
    def info(self):
        print('Patient name: ',self.name, '; Allergies: ', self.allergies, '; Assigned Bed: ', self.bed)
        return self
class hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self, patient):
        print('--New admit--')
        if len(self.patients) >= self.capacity:
            print('patient not admitted')
        else:
            self.patients.append(patient)
            patient.bed = self.patients.index(patient)
            print('new patient: ', patient.name, ' admitted to bed # ', patient.bed)
            # print('Patient: ', patient.name, ' successfully admitted to bed: ', patient.bed)
        return self

    def discharge(self, patient):
        print('--New discharge--')
        for x in self.patients:
            if x.name == patient:
                print('Patient found at index: ', self.patients.index(x))
                x.bed = 'none'
                self.patients[self.patients.index(x)]='empty'
        return self
    def info(self):
        print('Hospital name: ', self.name, '; Capacity: ' , self.capacity, 'Available beds', (self.capacity - len(self.patients)))
        return self
    def patientinfo(self):
        print('--Patients--')
        for x in self.patients:
            try:
                print('Patient name: ', x.name, '; Allergies: ', x.allergies, '; Assigned Bed: ', x.bed)
            except Exception as e:
                print("Bed: " , self.patients.index(x), " is empty")
        return self


stSomebody = hospital('St. Somebody', 10)
joe = patient('Joe', 'none')
dan = patient('Dan', 'seasonal')
ted = patient('Ted', 'sulfate')
stSomebody.admit(joe).admit(dan).admit(ted).info()
stSomebody.patientinfo()
stSomebody.discharge('dan').discharge('Dan').patientinfo()
stSomebody.admit(dan).patientinfo()
