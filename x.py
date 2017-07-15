import random

class Patient:
    def __init__(self, priority):
        assert 0 <= priority <= 5
        self.priority = priority
    def __repr__(self):
        return 'Patient(priority={})'.format(self.priority)

def patients_in_minute():
    if random.randint(0, 1) == 0:
        return []
    else:
        return [Patient(random.randint(0, 5))]

def go():
    patients = []
    toppatient = None
    for minute in range(60):
        patients.extend(patients_in_minute())
        patients.sort(key=lambda p: p.priority)
        if toppatient is None and len(patients) > 0:
            toppatient = patients.pop()
        # allocatedoctor
    print(patients)

if __name__ == '__main__':
    go()
