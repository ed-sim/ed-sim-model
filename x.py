import pprint
import random

class Patient:
    def __init__(self, priority, minute):
        assert 0 <= priority <= 5
        self.priority = priority
        self.arrived = minute
        self.seen = None
        self.finished = None
    def __repr__(self):
        return 'Patient(priority={},arrived={},seen={},finished={})'.format(
                self.priority, self.arrived, self.seen, self.finished
        )

class Doctor:
    def __init__(self):
        self.patient = None

def patients_in_minute(minute):
    if random.randint(0, 1) == 0:
        return []
    else:
        return [Patient(random.randint(0, 5), minute)]

def did_patient_finish_with_doctor(minute, patient):
    return minute - patient.seen == 10

def go():
    patients = []
    finished_patients = []
    doctors = [Doctor(), Doctor()]
    for minute in range(60):
        patients.extend(patients_in_minute(minute))
        patients.sort(key=lambda p: p.priority)

        for doctor in doctors:
            if doctor.patient is None and len(patients):
                doctor.patient = patients.pop()
                doctor.patient.seen = minute
            if doctor.patient is None:
                continue
            patient = doctor.patient
            if did_patient_finish_with_doctor(minute, patient):
                patient.finished = minute
                finished_patients.append(patient)
                doctor.patient = None

    pprint.pprint(finished_patients)

if __name__ == '__main__':
    go()
