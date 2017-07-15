from __future__ import print_function
import pprint
import random

class Patient:
    def __init__(self, priority, treatment_duration):
        assert 0 <= priority <= 5
        self.priority = priority
        self.treatment_duration = treatment_duration
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

weekarrivals = 5000
reldayattends = [
    0.158055144,0.141951248,0.141242013,0.139010815,0.134600165,
    0.136450873,0.148717898
]
relhourattends = [
    0.021955416,0.017915919,0.014026032,0.012211999,
    0.01168836,0.010267056,0.012679533,0.018626571,
    0.034204817,0.054907241,0.059489078,0.065380012,
    0.06399611,0.063491173,0.06059246,0.06291143,
    0.064239228,0.06046155,0.064257929,0.060480251,
    0.054084381,0.044939408,0.037514961,0.029679084,
]
patientqueue = []
for day in range(7):
    for hour in range(24):
        numarrivals = int(weekarrivals * reldayattends[day] * relhourattends[hour])
        for _ in range(numarrivals):
            arrivaltime = round((24*60*day) + (60*hour) + (random.uniform(0, 1)*59))
            patientqueue.append(arrivaltime)
patientqueue.sort()

def patients_in_minute(minute):
    patients = []
    while patientqueue and patientqueue[0] == minute:
        arrivaltime = patientqueue.pop(0)
        priority = random.randint(0, 5)
        treatment_duration = max(random.normalvariate(20, 20), 1)
        patient = Patient(priority, treatment_duration)
        patient.arrived = minute
        patients.append(patient)
    return patients

def did_patient_finish_with_doctor(minute, patient):
    return minute - patient.seen >= patient.treatment_duration

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
    doctors = [Doctor() for i in range(12)]

    # TODO: add warmup - queue isn't empty at beginning of day
    for minute in range(0, 7*24*60):
        if minute % 60 == 0:
            print('At minute {}, {} patients in queue, {} finished patients'.format(
                minute, len(patients), len(finished_patients)
            ))
        sim_minute(minute, patients, finished_patients, doctors)

    print('Saw {} patients, {} remaining'.format(len(finished_patients), len(patients)))

if __name__ == '__main__':
    go()
