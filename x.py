import pprint
import random

class Patient:
    def __init__(self, priority, treatment_time):
        assert 0 <= priority <= 5
        self.priority = priority
        self.treatment_time = treatment_time
        self.arrived = None
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
        priority = random.randint(0, 5)
        treatment_time = random.normalvariate(20, 10)
        patient = Patient(priority, treatment_time)
        patient.arrived = minute
        return [patient]

def did_patient_finish_with_doctor(minute, patient):
    return minute - patient.seen >= patient.treatment_time

def sim_minute(minute, patients, finished_patients, doctors):
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

def go():
    patients = []
    finished_patients = []
    doctors = [Doctor() for i in range(7)]

    # Warmup
    for minute in range(200):
        sim_minute(minute, patients, finished_patients, doctors)
    finished_patients = []

    for minute in range(201, 250):
        sim_minute(minute, patients, finished_patients, doctors)

    pprint.pprint(finished_patients)

if __name__ == '__main__':
    go()
